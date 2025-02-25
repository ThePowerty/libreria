from django import forms
from django.forms import ModelForm
from books.models import Editorial


class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'nombre',
            'codigo_postal',
            'direccion',
            'email',
            'fecha_fundacion',
        ]
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre