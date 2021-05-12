from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets
from apps.users.models import Profile
from apps.courses.permissions import IsTeacherOrReadOnly
from .models import Test, Question, TestResult
from . import serializers
from .utils import write_student_answer, calculate_result, check_attempts
from apps.courses.models import Course


class TestView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]
    serializer_class = serializers.TestSerializer
    queryset = Test.objects.all()
    permission_classes_by_action = {
        'retrieve': [IsAuthenticated]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


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
            if check_attempts(profile, test):
                result = calculate_result(student_answers)
                test_result = TestResult.objects.create(result=result, profile=profile, test=test)
                write_student_answer(student_answers, test_result)
                return Response(result, status=status.HTTP_201_CREATED)
            return Response('You have run out of attempts', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestResultView(APIView):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        test_result = TestResult.objects.filter(profile=profile)
        serializer = serializers.TestResultSerializer(test_result, many=True)
        return Response(serializer.data)


class TestCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        tests = Test.objects.filter(course=course)
        serializer = serializers.TestCourseSerializer(tests, many=True)
        return Response(serializer.data)
