from django.conf.urls import url, include
from profiles.api.views import (
    StudentListAPIView, ParentListAPIView, TeacherListAPIView
)

student_urlpatterns = [
    url(r'^$', StudentListAPIView.as_view()),
]

parent_urlpatterns = [
    url(r'^$', ParentListAPIView.as_view()),
]

teacher_urlpatterns = [
    url(r'^$', TeacherListAPIView.as_view())
]
