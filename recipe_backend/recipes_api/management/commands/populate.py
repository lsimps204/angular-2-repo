from django.core.management.base import BaseCommand
from django.db import IntegrityError

from recipes_api import factories, models

class Command(BaseCommand):
    help = 'Loads dummy data'

    # Creates fake data unless the DB is too bloated.
    def handle(self, *args, **kwargs):
        changes = factories.create_fake_data()
        print("Database changes entered") if changes else print("No changes made. Consider clearing the database")
