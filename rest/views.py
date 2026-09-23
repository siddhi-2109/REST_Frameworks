from django.shortcuts import render
from django.http import JsonResponse
from rest_app.models import student

# Create your views here.
def viewstudent(request):
    stu = student.objects.all()
    student_list = list(stu.values())
    return JsonResponse(student_list,safe=False)