""" Celery tasks """

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from django.conf import settings

import os, glob

from recipes_api import factories, models
from recipes_api.celery_helpers import BackupHelper

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
def task_backup_sqlite_database():
    """ Backs up the SQLite database file. We aim to keep one backup file at a time """
    sqlite_dir = os.path.abspath(settings.BASE_DIR)
    os.chdir(sqlite_dir)
    existing_files = glob.glob("*.sqlite3*")
    backup_helper = BackupHelper()

    # Check how many existing backups there are.
    # If none, then throw warning
    if len(existing_files) == 0:
        logger.warning("Cannot perform backup as no database file currently exists")
        return

    # If one, then do the backup.
    elif len(existing_files) == 1:
        backup_helper.make_backup()

    # If two (or more, for whatever reason), then backup and remove oldest
    elif len(existing_files) >= 2:
        backup_helper.make_backup()
        backup_helper.remove_older_backups()

    logger.info("Database backed up")

# Not intuitive or useful in any way... just a test
@periodic_task(
    run_every=(crontab(minute='*/2')),
    name="cron.test", # It's a good idea to namespace task names
    ignore_result=True
)
def sum_of_ingredients(break_point=None):
    from django.db.models import Sum
    s = models.RecipeIngredient.objects.aggregate(amt=Sum('amount'))['amt']
    logger.info("A total of: {} ingredients used in recipes... useless statistic!".format(s))