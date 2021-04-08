from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins
from apps.users.models import Profile
from . import serializers
from .models import Course, Module, Material
from .permissions import IsTeacherOrReadOnly


class CourseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CourseSerializer

    @action(methods=['POST', ], detail=False)
    def add_course(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        profile = Profile.objects.get(user=request.user)
        if serializer.is_valid():
            if profile.role == 'teacher':
                serializer.save(teacher=profile)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Course can add only teacher', status=status.HTTP_400_BAD_REQUEST)


class CourseEditView(generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


class CourseDetailView(generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer
    permission_classes = [IsAuthenticated]


class EnrollCourse(APIView):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        profile = Profile.objects.get(user=request.user)
        course.students.add(profile)
        return Response(status=status.HTTP_201_CREATED)


class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly,)


class MaterialView(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]
