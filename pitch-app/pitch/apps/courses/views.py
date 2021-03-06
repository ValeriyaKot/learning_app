from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins
from apps.users.models import Profile
from . import serializers
from .models import Course, Module, Material
from .permissions import IsTeacherOrReadOnly


class CourseView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.CourseSerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsTeacherOrReadOnly],
    }

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {
        'retrieve': [AllowAny],
        'update': [IsAuthenticated, IsTeacherOrReadOnly],
        'destroy': [IsAuthenticated, IsTeacherOrReadOnly],
        'partial_update': [IsAuthenticated, IsTeacherOrReadOnly],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class EnrollCourse(APIView):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        profile = Profile.objects.get(user=request.user)
        if course.teacher != profile:
            course.students.add(profile)
            return Response(status=status.HTTP_201_CREATED)
        return Response('Teacher cannot enroll in his course', status=status.HTTP_400_BAD_REQUEST)


class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]
    permission_classes_by_action = {
        'retrieve': [IsAuthenticated]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class MaterialView(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


class TeacherCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        courses = Course.objects.filter(teacher=profile)
        serializer = serializers.TeacherCourseSerializer(courses, many=True)
        return Response(serializer.data)


class StudentEnrolledCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        courses = Course.objects.filter(students=profile)
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)
