from django.shortcuts import render

from books.models import Libro

def libros_view(request):
    libros = Libro.objects.all()

    context = {
        "libros": libros,
        "titulo": "Lista de libros",
    }
    return render(request, 'libros/libros.html', context)