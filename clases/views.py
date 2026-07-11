from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm  
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'clases/inicio.html')


def instructor(request):
    return render(request, 'clases/instructor.html')

def cursos_precios(request):
    return render(request, 'clases/cursos.html')

def equipamiento(request):
    return render(request, 'clases/equipamiento.html') 


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect('cursos_precios') 
    else:
        form = RegistroUsuarioForm()

    return render(request, 'clases/registro.html', {'form': form}) 


@login_required(login_url='login') 
def reservar(request):
    return render(request, 'clases/reserva_confirmada.html') 