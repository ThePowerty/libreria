from django.shortcuts import render

from books.models import Autor, Libro, Editorial, Contacto
from books.forms import SearchForm
from .form import ContactModelFormCreate

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