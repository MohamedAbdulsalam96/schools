from django.conf.urls import url, include
from profiles.views import teacher_views

urlpatterns = [
    url(r'^$', teacher_views.get_teacher_list, name="teacher-list"),
	url(r'^list$', teacher_views.get_teacher_list, name="teacher-list"),
	url(r'^new/$', teacher_views.save_update_teacher, name="new-teacher"),
	url(r'^(?P<id>[\d]+)/$', teacher_views.get_teacher_profile, name="teacher-profile"),
	url(r'^(?P<id>[\d]+)/edit$', teacher_views.save_update_teacher, name="update-teacher"),
	url(r'^(?P<id>[\d]+)/delete$', teacher_views.delete_teacher, name="delete-teacher"),
]
