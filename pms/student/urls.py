from django.contrib import admin
from django.urls import path,include
from .views import StudentCreateView,StudentListView,StudentDetailView,StudentDeleteView,StudentUpdateView

#localhost:8000/student/create/
urlpatterns = [
 path("create/",StudentCreateView.as_view(),name="create_student"),
 path("list/",StudentListView.as_view(),name="list_student"),
 path("detail/<int:pk>/",StudentDetailView.as_view(),name="detail_student"),
 path("delete/<int:pk>/",StudentDeleteView.as_view(),name="delete_student"),
 path("update/<int:pk>/",StudentUpdateView.as_view(),name="update_student"),
]