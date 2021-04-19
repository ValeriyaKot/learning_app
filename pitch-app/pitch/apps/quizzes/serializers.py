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


class TestResultSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField(read_only=True)
    profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.TestResult
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)
    test = serializers.StringRelatedField(read_only=True)
    question = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.StudentAnswer
        fields = '__all__'
