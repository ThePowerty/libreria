from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from books.models import Libro
from django.urls import reverse_lazy

def libros_view(request):
    libros = Libro.objects.all()

    context = {
        "libros": libros,
        "titulo": "Lista de libros",
    }
    return render(request, 'libros/libros.html', context)

class LibrosListView(ListView):
    model = Libro
    template_name = "libros/libros.html"
    context_object_name = "libros"

class LibroDetail(DetailView):
    model = Libro
    template_name = "libros/libro_detail.html"
    context_object_name = "libro"

class LibroCreateView(CreateView):
    model = Libro
    fields=[
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"
    ]
    template_name = "libros/libro_create.html"
    success_url = reverse_lazy('books:libros_list')

class LibroUpdateView(UpdateView):
    model = Libro
    fields=[
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"
    ]
    template_name = "libros/libro_update.html"
    def get_success_url(self):
        return reverse_lazy('books:libro_detail', kwargs={'pk': self.object.pk})
    
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/libro_delete.html"
    success_url = reverse_lazy('books:libros_list')