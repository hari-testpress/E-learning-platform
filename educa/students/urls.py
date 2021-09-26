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
        views.student_enroll_course,
        name="enroll_course",
    ),
]
