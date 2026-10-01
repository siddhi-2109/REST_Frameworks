from django.urls import path
from . import views

urlpatterns = [
    path("student/",views.viewstudent),
    path("student/<int:pk>/",views.viewstudentbyid)
]
