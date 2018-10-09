from django.conf.urls import url, include
from academic.views import subject_views

urlpatterns = [
    url(r'^$', subject_views.get_subject_list, name='subject-list'),
    url(r'^list$', subject_views.get_subject_list, name='subject-list'),
    url(r'^new/$', subject_views.save_update_subject, name="new-subject"),
    url(r'^(?P<subject>[\w_ ]+)/edit$', subject_views.save_update_subject, name="update-subject"),
    url(r'^(?P<subject>[\w_ ]+)/delete$', subject_views.delete_subject, name="delete-subject"),
]
