from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from .models import *

def asosiy(request):
    regions = Region.objects.all()
    departments = Department.objects.all()
    employees = Employee.objects.all()

    context = {
        "regions": regions,
        "departments": departments,
        "employees": employees
    }
    return render(request, "asosiy.html", context)

def add_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Viloyat muvaffaqiyatli qo'shildi!!!")
            return redirect('asosiy')
    else:
        form = RegionForm()

    context = {'form': form}
    return render(request, 'add_region.html', context)


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tashkilot muvaffaqiyatli qo'shildi!!!")
            return redirect('asosiy')
    else:
        form = DepartmentForm()

    context = {'form': form}
    return render(request, 'add_department.html', context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee muvaffaqiyatli qo'shildi!!!")
            return redirect('asosiy')
    else:
        form = EmployeeForm()
    return render(request, "add_employee.html", {'form': form})

