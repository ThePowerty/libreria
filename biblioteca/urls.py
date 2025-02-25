from django.contrib import admin
from django.urls import path, include
from .views import home_view, contact_view, search_view

urlpatterns = [
    path("", home_view, name="home"),
    path("", include('books.urls', namespace="books")),
    path("buscar/", search_view, name="search"),
    path("contacta-con-nosotros/", contact_view, name="contacto"),
    path('admin/', admin.site.urls),
]
