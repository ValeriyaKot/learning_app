from rest_framework import serializers
from . import models
from apps.users.serializers import ProfileSerializer


class MaterialSerializer(serializers.ModelSerializer):
    # module = serializers.StringRelatedField()

    class Meta:
        model = models.Material
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(read_only=True)
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = models.Module
        fields = '__all__'

    # def create(self, validated_data):
    #     materials_data = validated_data.pop('materials')
    #     module = models.Module.objects.create(**validated_data)
    #     for material in materials_data:
    #         models.Material.objects.create(module=module, **material)
    #     return module


class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        exclude = ['students']

    # def create(self, validated_data):
    #     modules_data = validated_data.pop('modules')
    #     course = models.Course.objects.create(**validated_data)
    #     for module in modules_data:
    #         models.Module.objects.create(course=course, **module)
    #     return course
    #
    # def update(self, instance, validated_data):
    #     modules_data = validated_data.pop('modules')
    #     modules = instance.modules.all()
    #     modules = list(modules)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.save()
    #
    #     for module_data in modules_data:
    #         module = modules.pop(0)
    #         module.title = module_data.get('title', module.title)
    #         module.description = module_data.get('description', module.description)
    #         module.save()
    #     return instance



class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)
    students = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = models.Course
        fields = '__all__'


class EnrollCourseSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Course
        fields = ['students']