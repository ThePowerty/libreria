from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label="Introduce cualquier cadena de texto",
        max_length=100
    )