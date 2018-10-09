from django.conf.urls import url, include
from academic.views import course_views

urlpatterns = [
    url(r'^$', course_views.get_course_list, name='course-list'),
    url(r'^list$', course_views.get_course_list, name='course-list'),
    url(r'^new/$', course_views.save_update_course, name="new-course"),
    url(r'^(?P<course>[\w_ ]+)/edit$', course_views.save_update_course, name="update-course"),
    url(r'^(?P<course>[\w_ ]+)/delete$', course_views.delete_course, name="delete-course"),
]
