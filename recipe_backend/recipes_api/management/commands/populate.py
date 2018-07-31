from django.core.management.base import BaseCommand
from django.db import IntegrityError

from recipes_api.tasks import populate_database

class Command(BaseCommand):
    help = 'Loads dummy data'

    # Creates fake data unless the DB is too bloated.
    def handle(self, *args, **kwargs):
        populate_database.delay()