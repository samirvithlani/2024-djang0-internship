from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #localhost:8000/employee/create
    path("create/",views.create_employee),
    path("list/",views.getall_employee),
    #localhost:8000/employee/delete/1
    path("delete/<int:id>/",views.delete_employee,name = "delete_employee"),
    path("detail/<int:id>/",views.detail_employee,name = "detail_employee"),
    path("update/<int:id>/",views.update_employee,name = "update_employee")
]
   