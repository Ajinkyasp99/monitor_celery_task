import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')

app = Celery('celery_task')
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# if you need to ignore some task in monitoring task then just add ignore_result=True in @task

# @task(bind=True, ignore_result=True)
# def process_meter_reading_logs_for_alert(self, request_data, all_alert_conditions, plant_id):
#     """
#     Send Real time Alerts
#     :param self:
#     :param request_data:
#     :param all_alert_conditions:
#     :param plant_id:
#     :return:
#     """
#     plant_obj = accounts_public.get_plant_details(plant_id=plant_id)
#     if plant_obj.is_active:  # only process alert for active plant
#         with context_manager.SetTenantModel(plant_obj.organisation):
#             alert_public.tasks_send_real_time_alerts_based_on_request_data(
#                 request_data=request_data, all_alert_conditions=all_alert_conditions, plant_obj=plant_obj
#             )