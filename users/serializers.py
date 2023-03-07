from rest_framework import serializers
from users.models import Students, StudentDetail


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    student = StudentsSerializer()
    class Meta:
        model= StudentDetail
        fields = '__all__'