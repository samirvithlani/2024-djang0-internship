from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView


urlpatterns = [

#localhost:8000/user/manager_register/
path("manager_register/",ManagerRegisterView.as_view(),name="manager_register"),
path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
]
