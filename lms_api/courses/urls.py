from django.urls import path

from .views import (CourseList, CourseDetail, CourseWeekList, 
                    CourseWeekDetail, CourseMaterialList,
                    CourseAttendanceList, CourseEnrolledList)

urlpatterns = [
    path("", CourseList.as_view(), name="course_list"),
    path("<int:pk>/", CourseDetail.as_view(), name="course_detail"),
    path("<int:course_id>/weeks/", CourseWeekList.as_view(), name="course_week_list"),
    path("<int:course_id>/weeks/<int:pk>/", CourseWeekDetail.as_view(), name="course_week_detail"),
    path("<int:course_id>/weeks/<int:course_week_id>/materials/", CourseMaterialList.as_view(), name="course_material_list"),
    path("<int:course_id>/weeks/<int:course_week_id>/attendances/", CourseAttendanceList.as_view(), name="course_attendances"),
    path("<int:course_id>/students/", CourseEnrolledList.as_view(), name="course_students"),
]