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
    # materials = MaterialSerializer(many=True, read_only=True)

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
    # modules = ModuleSerializer(many=True)

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

    class Meta:
        model = models.Course
        fields = '__all__'




class AnswerSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    class Meta:
        model = models.Answer
        fields = '__all__'

    def get_percent(self, obj):
        total = models.StudentAnswer.objects.filter(question=obj.question).count()
        current = models.StudentAnswer.objects.filter(question=obj.question, answer=obj).count()
        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, source='answer_set', )

    class Meta:
        model = models.Question
        fields = '__all__'


class StudentAnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()

    def validate_answers(self, answers):
        if not answers:
            raise serializers.ValidationError("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        user = self.context.user
        for question_id in answers:
            question = models.Question.objects.get(pk=question_id)
            answers = answers[question_id]
            for answer_id in answers:
                answer = models.Answer.objects.get(pk=answer_id)
                models.Answer(user=user, question=question, answer=answer).save()
                user.is_answer = True
                user.save()