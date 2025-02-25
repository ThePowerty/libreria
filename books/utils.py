from django.db import models

# Modelo para Editoriales
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.URLField()
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre
    
# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    sitio_web = models.URLField()
    premios = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    idioma = models.CharField(max_length=100)
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo