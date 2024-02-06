from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
#function based views

def create_employee(request):
    
    context = {} #empty dictionary
    
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context["form"] = form #passing form to context to create form in template    
    
    return render(request,"employee/employee_create.html",context)

def getall_employee(request):
    context = {} #empty dictionary
    employees = Employee.objects.all().values() #select * from employee
    print(employees)
    context["employees"] = employees
    return render(request,"employee/employee_list.html",context)