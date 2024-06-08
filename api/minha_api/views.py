from django.shortcuts import render
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer

class EmployeesListCreate(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class EmployeesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer