from rest_framework.serializers import ModelSerializer
from profiles.models import Student, Teacher, Parent

class StudentSerializer(ModelSerializer):
    class Meta(object):
        model = Student
        fields = [
            "user",
			"first_name",
			"last_name",
			"date_of_joining",
			"roll_no",
			"course",
			"department",
			"created_by"
        ]

class ParentSerializer(ModelSerializer):
    class Meta(object):
        model = Parent
        fields = [
            "user",
			"first_name",
			"last_name",
            "mobile"
        ]

class TeacherSerializer(ModelSerializer):
    class Meta(object):
        model = Teacher
        fields = [
            "user",
			"first_name",
			"last_name",
            "mobile"
        ]
