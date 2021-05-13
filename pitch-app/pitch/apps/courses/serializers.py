from rest_framework import serializers
from apps.users.serializers import ProfileSerializer
from . import models
from apps.quizzes.serializers import TestSerializer


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Material
        fields = '__all__'


class ModuleMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Material
        fields = ['text']


class ModuleSerializer(serializers.ModelSerializer):
    materials = ModuleMaterialSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'

    def create(self, validated_data):
        materials_data = validated_data.pop('materials')
        module = models.Module.objects.create(**validated_data)
        for material_data in materials_data:
            models.Material.objects.create(module=module, **material_data)
            return module

    def update(self, instance, validated_data):
        materials_data = validated_data.pop('materials')
        materials = instance.materials.all()
        materials = list(materials)
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        for material_data in materials_data:
            material = materials.pop(0)
            material.text = material_data.get('text', material.text)
            material.save()
            return instance


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


class TeacherCourseSerializer(serializers.ModelSerializer):
    students = ProfileSerializer(read_only=True, many=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'
