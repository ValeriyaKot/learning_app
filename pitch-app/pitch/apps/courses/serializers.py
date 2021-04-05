from rest_framework import serializers
from .models import Answer, Question, StudentAnswer, Course
from apps.users.serializers import ProfileSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer(read_only=True)

    class Meta:
        model = Course
        exclude = ['students']


class AnswerSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = '__all__'

    def get_percent(self, obj):
        total = StudentAnswer.objects.filter(question=obj.question).count()
        current = StudentAnswer.objects.filter(question=obj.question, answer=obj).count()
        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, source='answer_set', )

    class Meta:
        model = Question
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
            question = Question.objects.get(pk=question_id)
            answers = answers[question_id]
            for answer_id in answers:
                answer = Answer.objects.get(pk=answer_id)
                Answer(user=user, question=question, answer=answer).save()
                user.is_answer = True
                user.save()