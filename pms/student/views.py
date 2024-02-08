from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student
from .forms import StudentForm


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    success_url = "/student/list/"


class StudentListView(ListView):
    model = Student # SELECT * FROM student_student
    context_object_name = "students"
    template_name = "student/student_list.html"    

class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "student/student_detail.html"

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/student_delete.html"    
    success_url = "/student/list/"


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = "/student/list/"
    template_name = "student/student_update_form.html"    