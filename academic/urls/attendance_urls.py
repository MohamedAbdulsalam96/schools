from django.conf.urls import url, include
from academic.views import attendance_views

urlpatterns = [
    url(r'^$', attendance_views.get_attendance_list, name='attendance-list'),
    url(r'^list$', attendance_views.get_attendance_list, name='attendance-list'),
    url(r'^new/$', attendance_views.save_update_attendance, name="new-attendance"),
    url(r'^(?P<id>[\d]+)/edit$', attendance_views.save_update_attendance, name="update-attendance"),
    url(r'^(?P<id>[\d]+)/delete$', attendance_views.delete_attendance, name="delete-attendance"),
]
