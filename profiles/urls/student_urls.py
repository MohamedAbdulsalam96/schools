from django.conf.urls import url, include
from profiles.views import student_views

urlpatterns = [
    url(r'^$', student_views.get_student_list, name="student-list"),
    url(r'^list$', student_views.get_student_list, name="student-list"),
    url(r'^new/$', student_views.save_update_student, name="new-student"),
    url(r'^(?P<prn>[\d]+)/$', student_views.get_student_profile,
        name="student-profile"),
    url(r'^(?P<prn>[\d]+)/edit$', student_views.save_update_student,
        name="update-student"),
    url(r'^(?P<prn>[\d]+)/delete$', student_views.delete_student,
        name="delete-student"),
]
