from celery import shared_task
from time import sleep


@shared_task(bind=True)
def go_inside_sleep(self, sec):
    sleep(sec)
    return "My celery working done"
