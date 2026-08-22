from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Favorito


def inicio(request):
    return render(request, 'index.html')

def propiedades(request):
    return render(request, 'propiedades.html')

def favoritos(request):
    if not request.user.is_authenticated:
        return redirect('login')

    favoritos = Favorito.objects.filter(usuario=request.user)

    return render(request, 'favoritos.html', {
        'favoritos': favoritos
    })


def agregar_favorito(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.POST.get('imagen')
        precio = request.POST.get('precio')
        detalle_url = request.POST.get('detalle_url')

        Favorito.objects.create(
            usuario=request.user,
            nombre=nombre,
            imagen=imagen,
            precio=precio,
            detalle_url=detalle_url
        )

    return redirect('favoritos')

def nosotros(request):
    return render(request, 'nosotros.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('inicio')

        return render(request, 'login.html', {
            'error': 'Usuario o contraseña incorrectos.'
        })

    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            return render(request, 'registro.html', {
                'error': 'Este correo ya está registrado.'
            })

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=nombres,
            last_name=apellidos
        )

        auth_login(request, usuario)

        return redirect('inicio')

    return render(request, 'registro.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')