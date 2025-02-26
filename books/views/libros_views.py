from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from books.models import Libro
from django.urls import reverse_lazy

class LibrosListView(ListView):
    model = Libro
    template_name = "libros/LibroList.html"
    context_object_name = "libros"


class LibroDetail(DetailView):
    model = Libro
    template_name = "libros/LibroDetail.html"
    context_object_name = "libro"


class LibroCreateView(CreateView):
    model = Libro
    fields=[
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"
    ]
    template_name = "libros/LibroCreate.html"
    success_url = reverse_lazy('libro:list')


class LibroUpdateView(UpdateView):
    model = Libro
    fields=[
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"
    ]
    template_name = "libros/LibroUpdate.html"
    def get_success_url(self):
        return reverse_lazy('libro:detail', kwargs={'pk': self.object.pk})


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/LibroDelete.html"
    success_url = reverse_lazy('libro:list')