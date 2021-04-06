from django.http import Http404

from . import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins
from .models import Question, Course, Module, Material
from apps.users.models import Profile
from rest_framework.decorators import action
from .permissions import IsTeacherOrReadOnly


class CourseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CourseSerializer

    @action(methods=['POST', ], detail=False)
    def add_course(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        teacher = Profile.objects.get(user=request.user)
        if serializer.is_valid():
            if teacher.role == 'teacher':
                serializer.save(teacher=teacher)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


class MaterialView(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.QuestionSerializer

    def get(self, request):
        questions = Question.objects.filter(visible=True)
        last_point = serializers.QuestionSerializer(questions, many=True)
        return Response(last_point.data)


class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AnswerSerializer

    def post(self, request):
        answer = serializers.AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})