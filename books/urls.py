from django.urls import path

from .views import editoriales_view, autores_view, autor_detail, libros_view, editorial_create, editorial_detail, AutorList, AutorDetail, EditorialList, EditorialDetail, LibroCreateView, LibrosListView, LibroUpdateView, LibroDetail, LibroDeleteView

app_name = "books"

urlpatterns = [
    path("editoriales/", editoriales_view, name="editorial_list"),
    path("editoriales/list/", EditorialList.as_view(), name="editorial_list_ccbv"),
    path("editoriales/detalle/ccbv/<pk>/", EditorialDetail.as_view(), name="editorial_detail_ccbv"),
    path("editoriales/detalle/<int:id>/", editorial_detail, name="editorial_detail"),
    path("editoriales/create/", editorial_create, name="editorial_create"),
    path("autores/", autores_view, name="autor_list"),
    path("autores/<int:id>/", autor_detail, name="autor_detail"),
    path("autores/list", AutorList.as_view(), name="autor_list_ccbv"),
    path("autores/detail/<pk>", AutorDetail.as_view(), name="autor_detail_ccbv"),
    path("libros/", libros_view, name="libros_list"),
    path("libros/list", LibrosListView.as_view(), name="libros_list"),
    path("libros/detail/<pk>", LibroDetail.as_view(), name="libro_detail"),
    path("libros/editar/<pk>/", LibroUpdateView.as_view(), name="libro_update"),
    path("libros/nuevo", LibroCreateView.as_view(), name="libro_create"),
    path("libros/eliminar/<pk>", LibroDeleteView.as_view(), name="libro_delete"),
]