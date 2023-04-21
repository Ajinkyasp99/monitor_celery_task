from celery.result import AsyncResult
from celery_progress.backend import Progress
from django.http import HttpResponse
from celery_task import tasks


def get_progress(task_id):
    progress = Progress(AsyncResult(task_id))
    print(progress.get_info())
    return progress.get_info()


def index(request):
    tasks_data = tasks.go_inside_sleep.delay(5)

    return HttpResponse("Hello, world. You're at the polls index.", get_progress(tasks_data.task_id))
