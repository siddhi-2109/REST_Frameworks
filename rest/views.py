# from django.shortcuts import render
# from django.http import JsonResponse
from rest_app.models import student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def viewstudent(request):
    if request.method == "GET":
        # get all the data from the students
        students = student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        serializer=StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def viewstudentbyid(request, pk):
    try:
        students = student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(students)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer=StudentSerializer(students,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        




        
