import logging
from celery import shared_task
from celery.utils.log import get_task_logger
from car.models import Car

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")
    # Car.objects.create(vendor='Audi', vehicle_id='e844310a-5530-11ed-bdc3-0242ac120002', user_id=2)


def every_minute(sender):
    print("Finally!!")
