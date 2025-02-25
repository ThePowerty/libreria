from django.shortcuts import render
from datetime import date

from books.models import Autor


def autores_view(request):
    autores = Autor.objects.all()

    context = {
        "autores": autores,
        "titulo": "Lista de autores",
    }

    return render(request, "autores/autores.html", context)


def autor_detail(request, id):

    autores = Autor.objects.get(pk=id)

    context = {
        "autor": autores,
    }

    return render(request, "autores/autor_detail.html", context)