from rest_framework import serializers

from .models import Course, CourseWeek, CourseMaterial, CourseStudentsEnrolled, CourseAttendance


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "teacher",
        )
        model = Course

class CourseWeekSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = CourseWeek
        fields = '__all__'

class CourseMaterialSerializer(serializers.ModelSerializer):
    course_week = CourseWeekSerializer()
    class Meta:
        model = CourseMaterial
        fields = '__all__'

class CourseStudentsEnrolledSerializer(serializers.ModelSerializer):
    course = CourseSerializer
    class Meta:
        model = CourseStudentsEnrolled
        fields = '__all__'

class CourseAttendanceSerializer(serializers.ModelSerializer):
    course_week = CourseWeekSerializer
    class Meta:
        model = CourseAttendance
        fields = '__all__'