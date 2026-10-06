from django.urls import path
from . import views

urlpatterns = [
    path("student/",views.viewstudent),
    path("student/<int:pk>/",views.viewstudentbyid),


    # class based views path

    path("employee/",views.Employee.as_view()),
    path("employee/<int:pk>/",views.EmployeeDetails.as_view())

]
