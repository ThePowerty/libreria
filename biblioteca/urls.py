from django.contrib import admin
from django.urls import path, include
from .views import home_view, contact_view, search_view, login_view, register_view, logout_view


urlpatterns = [
    path("", home_view, name="home"),
    path("editorial/", include('books.urls.editorial_url', namespace='editorial')),
    path("autor/", include('books.urls.autor_url', namespace="autor")),
    path("libro/", include('books.urls.libro_url', namespace="libro")),
    path("buscar/", search_view, name="search"),
    path("contacta-con-nosotros/", contact_view, name="contacto"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
