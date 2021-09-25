from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    path(
        "register/",
        views.StudentRegistrationView.as_view(),
        name="registration",
    ),
    path(
        "enroll-course/",
        views.StudentEnrollCourseView.as_view(),
        name="enroll_course",
    ),
]
