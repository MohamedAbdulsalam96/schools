from profiles.models import Teacher
from rest_framework.generics import ListAPIView
from profiles.api.serializers import TeacherSerializer

class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
