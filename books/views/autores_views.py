from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Autor

class AutorListView(ListView):
    model = Autor
    template_name = "autores/AutorList.html"
    context_object_name = "autores"

class AutorDetailView(DetailView):
    model = Autor
    template_name = "autores/AutorDetail.html"
    context_object_name = "autor"

class AutorCreateView(CreateView):
    model = Autor
    fields=[
        'nombre',
        'apellido',
        'fecha_nacimiento',
        'nacionalidad',
        'email',
    ]
    template_name = "autores/AutorCreate.html"
    success_url = reverse_lazy('autor:list')


class AutorUpdateView(UpdateView):
    model = Autor
    fields=[
        'nombre',
        'apellido',
        'fecha_nacimiento',
        'nacionalidad',
        'email',
    ]
    template_name = "autores/AutorUpdate.html"
    def get_success_url(self):
        return reverse_lazy('autor:detail', kwargs={'pk': self.object.pk})


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "autores/AutorDelete.html"
    success_url = reverse_lazy('autor:list')