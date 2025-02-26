from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Autor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_model

class AutorListView(ListView):
    model = Autor
    template_name = "autores/AutorList.html"
    context_object_name = "autores"


class AutorDetailView(DetailView):
    model = Autor
    template_name = "autores/AutorDetail.html"
    context_object_name = "autor"


@method_decorator(login_required, name="dispatch")
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
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
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


@method_decorator(user_can_delete_model(Autor), name="dispatch")
class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "autores/AutorDelete.html"
    success_url = reverse_lazy('autor:list')