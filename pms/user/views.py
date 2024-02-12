from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import ManagerCreationForm,DeveloperCreationForm

# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerCreationForm
    template_name = 'user/manager_register.html'
    success_url = '/login/'


class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperCreationForm
    template_name = 'user/developer_register.html'
    success_url = '/login/'    