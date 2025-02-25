from django.shortcuts import render
from datetime import date
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

# Vistas CCBV
class AutorList(ListView):
    model = Autor
    template_name = "autores/autores.html"
    context_object_name = "autores"

class AutorDetail(DetailView):
    model = Autor
    template_name = "autores/autor_detail.html"
    context_object_name = "autor"