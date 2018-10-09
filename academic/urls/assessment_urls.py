from django.conf.urls import url, include
from academic.views import assessment_views

urlpatterns = [
    url(r'^$', assessment_views.get_assessment_list, name='assessment-list'),
    url(r'^list$', assessment_views.get_assessment_list, name='assessment-list'),
    url(r'^new/$', assessment_views.save_update_assessment, name="new-assessment"),
    url(r'^(?P<id>[\d]+)/edit$', assessment_views.save_update_assessment, name="update-assessment"),
    url(r'^(?P<id>[\d]+)/delete$', assessment_views.delete_assessment, name="delete-assessment"),
]
