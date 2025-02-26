from django.urls import path

from books.views import LibroCreateView, LibrosListView, LibroUpdateView, LibroDetail, LibroDeleteView

app_name = "libro"

urlpatterns = [
    path("list", LibrosListView.as_view(), name="list"),
    path("detail/<pk>", LibroDetail.as_view(), name="detail"),
    path("create/", LibroCreateView.as_view(), name="create"),
    path("update/<pk>/", LibroUpdateView.as_view(), name="update"),
    path("delete/<pk>", LibroDeleteView.as_view(), name="delete"),
]