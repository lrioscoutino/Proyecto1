from rest_framework import viewsets
from users.models import Students, StudentDetail
from users.serializers import (
    StudentsSerializer,
    StudentDetailSerializer
)


class StudentsViewSets(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class StudentDetailViewSets(viewsets.ModelViewSet):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
