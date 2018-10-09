from django.conf.urls import url, include
from academic.views import exam_views

urlpatterns = [
    url(r'^$', exam_views.get_exam_list, name='exam-list'),
    url(r'^list$', exam_views.get_exam_list, name='exam-list'),
    url(r'^new/$', exam_views.save_update_exam, name="new-exam"),
    url(r'^(?P<exam>[\w_ ]+)/edit$', exam_views.save_update_exam, name="update-exam"),
    url(r'^(?P<exam>[\w_ ]+)/delete$', exam_views.delete_exam, name="delete-exam"),
]
