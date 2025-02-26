from django.shortcuts import render
from django.urls import reverse
from books.models import Autor, Libro, Editorial, Contacto
from books.forms import SearchForm
from .form import ContactModelFormCreate, LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.core.mail import send_mail

def home_view(request):
    return render(request, 'general/home.html')

def search_view(request):
    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data['search']

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)

        context = {
            'autores': autores,
            'editoriales': editoriales,
            'libros': libros,
            'formulario': formulario
        }

        return render(request, "general/search.html", context)
    else:
        formulario = SearchForm()

    context = {
        'formulario' : formulario
    }

    return render(request, "general/search.html", context)


def contact_view(request):
    if request.POST:
        formulario = ContactModelFormCreate(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']

            message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

            Contacto.objects.create(
                nombre=nombre,
                email=email,
                comentario=comentario
            )
            success = send_mail(
                "Formulario de contacto de mi Web",
                message_content,
                "w.infanzon.98@gmail.com",
                ["w.infanzon.98@gmail.com"],
                fail_silently=False,
            )

            context = {
              'formulario' : formulario,
              'success' : success
            }
            return render(request, "general/contacto.html", context)
        else:
            context = {
              'formulario' : formulario,
            }
            return render(request, "general/contacto.html", context)
  
    formulario = ContactModelFormCreate()
    context = {
      'formulario' : formulario
    }
    return render(request, "general/contacto.html", context)

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('libreria:home'))
            else:
                context = {
                  'form': form,
                  'error': True,
                  'error_message': 'Usuario no válido' 
                }
                return render(request, "general/login.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "general/login.html", context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, "general/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('libreria:home'))

def register_view(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            user = User.objects.create_user(username, email, password2)
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            context = {
                'msj': 'Usuario creado correctamente'
            }

            return render(request, "general/register.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "general/register.html", context)
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, "general/login.html", context)