from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    success_url = "/student/list/"
    
    def form_valid(self, form):
        #print("age...",form.cleaned_data['age'])
        # if form.cleaned_data['age']<18:
        #     print("invalid age......")
        #     form.add_error('age', 'Age must be greater than 18')
        #     return self.form_invalid(form)
        # if form.cleaned_data['marks']<35:
        #     print("invalid marks......")
        #     form.add_error('marks', 'Marks must be greater than 35')
        #     return self.form_invalid(form)
        
        if form.cleaned_data['age']<18 or form.cleaned_data['marks']<35:
            print("invalid age or marks......")
            form.add_error(None, 'Age must be greater than 18 and Marks must be greater than 35')
            return self.form_invalid(form)
        
        
        return super().form_valid(form)
    
#method decorator
@method_decorator(login_required, name='dispatch')
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