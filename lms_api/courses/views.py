from django.shortcuts import render
from rest_framework import generics

from .models import Course, CourseWeek, CourseAttendance, CourseMaterial, CourseStudentsEnrolled
from .serializers import CourseSerializer, CourseWeekSerializer, CourseAttendanceSerializer, CourseMaterialSerializer, CourseStudentsEnrolledSerializer

# Create your views here.
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseWeekList(generics.ListAPIView):
    serializer_class = CourseWeekSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseWeek.objects.filter(course__id=course_id)

class CourseWeekDetail(generics.RetrieveAPIView):
    queryset = CourseWeek.objects.all()
    serializer_class = CourseWeekSerializer


class CourseMaterialList(generics.ListAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

class CourseAttendanceList(generics.ListAPIView):
    serializer_class = CourseAttendanceSerializer

    def get_queryset(self):
        course_week_id = self.kwargs['course_week_id']
        return CourseAttendance.objects.filter(course_week__id=course_week_id)
    
class CourseEnrolledList(generics.ListAPIView):
    serializer_class = CourseStudentsEnrolledSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseStudentsEnrolled.objects.filter(course__id=course_id)