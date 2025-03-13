from django.urls import path
from .views import asosiy, add_region, add_department, add_employee

urlpatterns = [
    path('', asosiy, name='asosiy'),
    path('region/add/', add_region, name='add_region'),
    path('department/add/', add_department, name='add_department'),
    path('employee/add/', add_employee, name='add_employee'),
]
