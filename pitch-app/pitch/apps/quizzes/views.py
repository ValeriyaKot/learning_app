from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from apps.users.models import Profile
from apps.courses.permissions import IsTeacherOrReadOnly
from .models import Test, Question, TestResult
from . import serializers


class TestView(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]
    serializer_class = serializers.TestSerializer


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]
    serializer_class = serializers.QuestionSerializer


class CheckResultView(APIView):

    def post(self, request):
        data = request.data
        student = request.user
        profile = Profile.objects.get(user=student)
        test = Test.objects.get(pk=data['test_id'])
        serializer = serializers.CheckResultSerializer(data=data)
        if serializer.is_valid():
            result = self.__calculate_result(data['answers'])
            TestResult.objects.create(result=result, profile=profile, test=test)
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def __calculate_result(self, student_answers):
        result = 0
        for student_answer in student_answers:
            question_id = student_answer['question_id']
            question = Question.objects.get(pk=question_id)
            for answer in question.answers.all():
                if answer.is_correct and answer.text == student_answer['answer']:
                    result += 1

        return result


class TestResultView(APIView):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        test_result = TestResult.objects.filter(profile=profile)
        serializer = serializers.TestResultSerializer(test_result, many=True)
        return Response(serializer.data)
