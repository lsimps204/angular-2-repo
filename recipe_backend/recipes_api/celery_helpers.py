import shutil, os, glob
from datetime import datetime
from celery.utils.log import get_task_logger

from django.utils import timezone

logger = get_task_logger(__name__)

# Helper class for dealing with backup operations
class BackupHelper:
    # Finds either the oldest existing backup, or the newest in the current directory
    def find_backup(self, oldest=False, newest=False):
        file_list = self.db_files()
        # Ensure the params are set appropriately, and return if not
        if not oldest and not newest:
            logger.error("find_backup() requires either the `oldest` or `newest` argument to be set")
            return None
        if oldest and newest:
            logger.error("Either `oldest` or `newest` should be set, but not both")
            return None
        # Check if the original database file exists
        if "db.sqlite3" in file_list:
            if oldest:
                return "db.sqlite3"
            elif newest:
                if len(file_list) == 1: 
                    return "db.sqlite3"
                else:
                    date_part = self.extract_datepart(file_list)
                    date_str = max(date_part).strftime("%Y-%m-%d %H-%M-%S")
                    for f in file_list:
                        if f.endswith(date_str):
                            return f
        else:
            date_part = self.extract_datepart(file_list)
            if oldest:
                date_str = min(date_part).strftime("%Y-%m-%d %H-%M-%S")
            elif newest:
                date_str = max(date_part).strftime("%Y-%m-%d %H-%M-%S")
            for f in file_list:
                if f.endswith(date_str):
                    return f
            return None

    # Backs up the most recent database file in the directory
    def make_backup(self):
        newest_backup = self.find_backup(newest=True)
        shutil.copy(newest_backup, self.generate_backup_name())

    # Removes older backups from the directory
    def remove_older_backups(self):
        all_db_backups = self.db_files()
        while len(all_db_backups) > 2:
            oldest_backup = self.find_backup(oldest=True)
            if oldest_backup is not None:
                os.remove(oldest_backup)
                all_db_backups.remove(oldest_backup)
            else:
                return
                
    # Adds current datetime to the standard SQLite3 filename
    @staticmethod
    def generate_backup_name():
        current_datetime = timezone.now().strftime("%Y-%m-%d %H-%M-%S")
        return "db.sqlite3_{}".format(current_datetime)

    @staticmethod
    def extract_datepart(file_list):
        # Extract the dates from the backup names, and find oldest/newest depending on the flag passed in. 
        date_part = ["{}".format(file.split("_")[1]) for file in file_list if "_" in file]
        date_part = [datetime.strptime(file_date, "%Y-%m-%d %H-%M-%S") for file_date in date_part]
        return date_part

    @staticmethod
    def db_files():
        return glob.glob("*.sqlite3*")