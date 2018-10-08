from django.conf.urls import url, include
from academic.views import department_views

urlpatterns = [
    url(r'^$', department_views.get_department_list, name='department-list'),
    url(r'^list$', department_views.get_department_list, name='department-list'),
    url(r'^new/$', department_views.save_update_department, name="new-department"),
    url(r'^(?P<id>[\d]+)/edit$', department_views.save_update_department, name="update-department"),
    url(r'^(?P<id>[\d]+)/delete$', department_views.delete_department, name="delete-department"),
]
