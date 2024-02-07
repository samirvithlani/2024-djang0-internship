from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
    path("create/",views.create_product,name="create_product"),
    path("list/",views.list_product,name="list_product"),
    path("detail/<int:id>/",views.detail_product,name="detail_product"),
    path("delete/<int:id>/",views.delete_product,name="delete_product"),
    path("update/<int:id>/",views.update_product,name="update_product")
]