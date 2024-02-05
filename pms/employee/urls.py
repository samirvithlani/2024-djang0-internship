from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #localhost:8000/employee/create
    path("create/",views.create_employee)
]
   