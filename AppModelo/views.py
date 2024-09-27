from django.shortcuts import render
from AppModelo.models import Employee

# Create your views here.
def EmployeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados':empleados}
    return render(request, 'appTemplate/empleados.html', data)