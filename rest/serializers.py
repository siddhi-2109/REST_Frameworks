from rest_framework import serializers
from rest_app.models import student
from employee.models import Employees


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"  