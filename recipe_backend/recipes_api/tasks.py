""" Celery tasks """

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from django.utils import timezone
from django.conf import settings

import shutil, os, glob
from datetime import datetime

from recipes_api import factories, models

logger = get_task_logger(__name__)

@shared_task
def populate_database():
    logger.info('Populating...')
    changes = factories.create_fake_data()
    logger.info("CEL: Database changes entered") if changes else logger.info("CEL: No changes made. Consider clearing the database")

@shared_task
def delete_all_recipes():
    models.Recipe.objects.all().delete()

# A Celery periodic task designed to run every minute, updating the SQLite database file
@periodic_task(
    run_every=(crontab(minute='*')),
    name="task_backup_sqlite_database",
    ignore_result=True
)
def task_update_sqlite_database():
    """ Backs up the SQLite database file. We aim to keep one backup file at a time """
    sqlite_dir = os.path.abspath(settings.BASE_DIR)
    os.chdir(sqlite_dir)
    existing_files = glob.glob("*.sqlite3*")

    # Check how many existing backups there are.
    # If none, then throw warning
    if len(existing_files) == 0:
        logger.warning("Cannot perform backup as no database file currently exists")
        return

    # If one, then do the backup.
    elif len(existing_files) == 1:
        current_file = existing_files[0]
        shutil.copy(current_file, generate_backup_name())

    # If two, then backup and remove oldest
    elif len(existing_files) == 2:
        newest_backup = find_backup(existing_files, newest=True)
        shutil.copy(newest_backup, generate_backup_name())
        all_db_files = glob.glob("*.sqlite3*")
        remove_older_backups(all_db_files)

    # If (for some reason) there's more than two, remove the older backups until only two exist
    elif len(existing_files) > 2:
        newest_backup = find_backup(existing_files, newest=True)
        shutil.copy(newest_backup, generate_backup_name())
        all_db_files = glob.glob("*.sqlite3*")
        remove_older_backups(all_db_files)

    logger.info("Database backed up")

# Adds current datetime to the standard SQLite3 filename
def generate_backup_name():
    current_datetime = timezone.now().strftime("%Y-%m-%d %H-%M-%S")
    return "db.sqlite3_{}".format(current_datetime)

# Finds either the oldest existing backup, or the newest in the current directory
def find_backup(file_list, oldest=False, newest=False):

    # Ensure the params are set appropriately, and return if not
    if not oldest and not newest:
        logger.error("find_backup() requires either the `oldest` or `newest` argument to be set")
        return None
    if oldest and newest:
        logger.error("Either `oldest` or `newest` should be set, but not both")
        return None
    # Check if the original database file exists, delete if so
    if "db.sqlite3" in file_list:
        return "db.sqlite3"
    else:
        # Extract the dates from the backup names, and find oldest/newest depending on the flag passed in. 
        # Return the file.
        date_part = ["{}".format(file.split("_")[1]) for file in file_list if "_" in file]
        date_part = [datetime.strptime(file_date, "%Y-%m-%d %H-%M-%S") for file_date in date_part]
        if oldest:
            date_str = min(date_part).strftime("%Y-%m-%d %H-%M-%S")
        elif newest:
            date_str = max(date_part).strftime("%Y-%m-%d %H-%M-%S")
        for f in file_list:
            if f.endswith(date_str):
                return f
        logger.error("This didn't work")

def remove_older_backups(all_db_files):
    while len(all_db_files) > 2:
        oldest_backup = find_backup(all_db_files, oldest=True)
        if oldest_backup is not None:
            os.remove(oldest_backup)
            all_db_files.remove(oldest_backup)
        else:
            return