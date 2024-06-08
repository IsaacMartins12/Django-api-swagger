# minha_api/urls.py

from django.urls import path
from .views import EmployeesListCreate, EmployeesRetrieveUpdateDestroy

urlpatterns = [
    path('employees/', EmployeesListCreate.as_view(), name='employees-list-create'),
    path('employees/<int:pk>/', EmployeesRetrieveUpdateDestroy.as_view(), name='employees-retrieve-update-destroy'),
]
