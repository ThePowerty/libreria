from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from books.models import Libro
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_model

class LibrosListView(ListView):
    model = Libro
    template_name = "libros/LibroList.html"
    context_object_name = "libros"


class LibroDetail(DetailView):
    model = Libro
    template_name = "libros/LibroDetail.html"
    context_object_name = "libro"


@method_decorator(login_required, name="dispatch")
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
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
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


@method_decorator(user_can_delete_model(Libro), name="dispatch")
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/LibroDelete.html"
    success_url = reverse_lazy('libro:list')