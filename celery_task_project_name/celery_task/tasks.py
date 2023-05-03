from celery import shared_task
from time import sleep


@shared_task(bind=True)
def go_inside_sleep(self, sec):
    sleep(sec)
    return "My celery working done"


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