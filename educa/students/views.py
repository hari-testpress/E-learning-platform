from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    template_name = "students/student/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("student_course_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password1"])
        login(self.request, user)
        return result


def student_enroll_course(request):
    form = CourseEnrollForm(request.POST)
    if form.is_valid():
        course = form.cleaned_data["course"]
        course.students.add(request.user)
        return redirect("students:student_course_detail", pk=course.id)
