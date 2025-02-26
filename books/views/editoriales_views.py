from books.models import Editorial
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EditorialListView(ListView):
    model = Editorial
    template_name = "editoriales/EditorialList.html"
    context_object_name = "editoriales"


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editoriales/EditorialDetail.html"
    context_object_name = "editorial"


class EditorialCreateView(CreateView):
    model = Editorial
    fields=[
        'nombre',
        'direccion',
        'email',
        'fecha_fundacion'
    ]
    template_name = "editoriales/EditorialCreate.html"
    success_url = reverse_lazy('editorial:list')


class EditorialUpdateView(UpdateView):
    model = Editorial
    fields=[
        'nombre',
        'direccion',
        'email',
        'fecha_fundacion'
    ]
    template_name = "editoriales/EditorialUpdate.html"
    def get_success_url(self):
        return reverse_lazy('editorial:detail', kwargs={'pk': self.object.pk})


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = "editoriales/EditorialDelete.html"
    success_url = reverse_lazy('editorial:list')