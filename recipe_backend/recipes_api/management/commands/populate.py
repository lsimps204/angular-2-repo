from django.core.management.base import BaseCommand
from django.db import IntegrityError

from recipes_api.tasks import populate_database
from recipes_api.factories import create_fake_data
import os

class Command(BaseCommand):
    help = 'Loads dummy data'

    # Creates fake data unless the DB is too bloated.
    def handle(self, *args, **kwargs):
        if os.environ.get('DOCKER_CONTAINER', None) is not None:
            populate_database.delay() # Within container: a Celery task
        else:
            create_fake_data() # Not a celery task