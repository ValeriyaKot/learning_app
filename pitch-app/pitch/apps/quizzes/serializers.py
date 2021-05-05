from rest_framework import serializers
from . import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ['text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = models.Question
        fields = '__all__'

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = models.Question.objects.create(**validated_data)
        for answer_data in answers_data:
            models.Answer.objects.create(question=question, **answer_data)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('answers')
        answers = instance.answers.all()
        answers = list(answers)
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        for answer_data in answers_data:
            answer = answers.pop(0)
            answer.text = answer_data.get('text', answer.text)
            answer.is_correct = answer_data.get('is_correct', answer.is_correct)
            answer.save()
        return instance


class StudentAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer = serializers.CharField()


class CheckResultSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    answers = StudentAnswerSerializer(many=True)


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Test
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(read_only=True)
    correct_answer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.StudentAnswer
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField(read_only=True)
    profile = serializers.StringRelatedField(read_only=True)
    student_answers = AnswersSerializer(read_only=True, many=True)

    class Meta:
        model = models.TestResult
        fields = '__all__'
        