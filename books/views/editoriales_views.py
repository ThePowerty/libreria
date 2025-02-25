from django.shortcuts import render

from books.models import Editorial

def editoriales_view(request):
    editoriales = Editorial.objects.all()

    context = {
        "editoriales": editoriales,
        "titulo": "Lista de editoriales",
    }
    return render(request, 'editoriales/editoriales.html', context)