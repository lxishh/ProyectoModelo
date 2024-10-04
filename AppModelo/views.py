from django.shortcuts import render
from AppModelo.models import Employee
from . import forms

# Create your views here.
def EmployeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados':empleados}
    return render(request, 'appTemplate/empleados.html', data)

# def userRegistrationView(request):
#     formulario = forms.UserRegistrationForm()
#     data = {'form':formulario}
#     return render(request, 'appTemplate/userRegistration.html', data)

def userRegistrationView(request):
    form = forms.UserRegistrationForm()

    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form es Valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("Fono: ", form.cleaned_data['fono'])
            
    data = {'form':form}
    return render(request, 'appTemplate/userRegistration.html', data)