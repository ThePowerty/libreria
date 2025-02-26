from django.forms.models import BaseModelForm
from django.http import HttpResponse
from books.models import Editorial
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_model

class EditorialListView(ListView):
    model = Editorial
    template_name = "editoriales/EditorialList.html"
    context_object_name = "editoriales"


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editoriales/EditorialDetail.html"
    context_object_name = "editorial"

@method_decorator(login_required, name="dispatch")
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
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
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


@method_decorator(user_can_delete_model(Editorial), name="dispatch")
class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = "editoriales/EditorialDelete.html"
    success_url = reverse_lazy('editorial:list')