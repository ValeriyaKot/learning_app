from rest_framework import serializers
from apps.users.serializers import ProfileSerializer
from . import models
from apps.quizzes.serializers import TestSerializer


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ['text']


class ModuleSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'

    def create(self, validated_data):
        materials_data = validated_data.pop('materials')
        module = models.Module.objects.create(**validated_data)
        for material_data in materials_data:
            models.Material.objects.create(module=module, **material_data)
        return module


class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        exclude = ['students']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    students = ProfileSerializer(read_only=True, many=True)
    modules = ModuleSerializer(many=True, read_only=True)
    tests = TestSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'
