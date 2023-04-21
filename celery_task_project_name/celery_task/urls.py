from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("monitor-task/", include("monitor_task.urls")),
    path("admin/", admin.site.urls),
]
