from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from apps.users.models import Profile
from apps.courses.permissions import IsTeacherOrReadOnly
from .models import Test, Question, TestResult, StudentAnswer
from . import serializers
from .utils import write_student_answer, calculate_result


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
        student_answers = data['answers']
        test = Test.objects.get(pk=data['test_id'])
        serializer = serializers.CheckResultSerializer(data=data)
        if serializer.is_valid():
            result = calculate_result(student_answers)
            test_result = TestResult.objects.create(result=result, profile=profile, test=test)
            write_student_answer(student_answers, test_result)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestResultView(APIView):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        test_result = TestResult.objects.filter(profile=profile)
        serializer = serializers.TestResultSerializer(test_result, many=True)
        return Response(serializer.data)


class StudentAnswersView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.AnswersSerializer

    def get_queryset(self):
        student_answers = StudentAnswer.objects.all()
        return student_answers
