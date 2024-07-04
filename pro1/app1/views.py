from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

@login_required(login_url='/a2/lv/')
def employeeview(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/eform.html', {'form': form})

@login_required(login_url='/a2/lv/')
def showview(request):
    obj = Employee.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Employee.objects.get(eid=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/eform.html', {'form': form})

def deleteview(request, x):
    obj = Employee.objects.get(eid=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})
