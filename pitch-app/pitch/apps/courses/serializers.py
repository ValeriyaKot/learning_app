from rest_framework import serializers
from apps.users.serializers import ProfileSerializer
from . import models


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Material
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = models.Module
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        exclude = ['students']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    students = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = models.Course
        fields = '__all__'
