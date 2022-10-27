import os
from celery import Celery
from config.environment import SETTINGS_MODULE


os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
app = Celery('core',  broker="redis://:redis@localhost:6379/0")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# @app.on_after_configure.connect
# def schedule_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, test.s('ola'))

 
# @app.task
# def test(arg):
#     print(arg)
    