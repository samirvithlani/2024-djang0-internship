from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #localhost:8000/employee/create
    path("create/",views.create_employee),
    path("list/",views.getall_employee),
    #localhost:8000/employee/delete/1
    path("delete/<int:id>/",views.delete_employee,name = "delete_employee"),
]
   