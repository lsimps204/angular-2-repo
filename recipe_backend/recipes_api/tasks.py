""" Celery tasks """

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from recipes_api import factories

logger = get_task_logger(__name__)

@shared_task
def populate_database():
    logger.info('Populating...')
    changes = factories.create_fake_data()
    logger.info("CEL: Database changes entered") if changes else logger.info("CEL: No changes made. Consider clearing the database")