from profiles.models import Parent
from rest_framework.generics import ListAPIView
from profiles.api.serializers import ParentSerializer

class ParentListAPIView(ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
