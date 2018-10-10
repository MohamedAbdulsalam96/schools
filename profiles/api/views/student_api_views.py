from profiles.models import Student
from rest_framework.generics import ListAPIView
from profiles.api.serializers import StudentSerializer

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
