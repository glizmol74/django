from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Directores(models.Model):
    director = models.CharField(max_length=50, help_text='Ingrese el Nombre del Director')
    informacion = models.TextField(max_length=1000, help_text='Ingrese información del Director', null=True)
    fecha_nacimiento = models.DateField(help_text='Fecha de Nacimiento', null=True)
    foto = models.ImageField(upload_to='directores/fotos/', null=True)

    def __str__(self):
        txt = "{0} ({1})"
        fn =self.fecha_nacimiento
        ini = datetime(fn.year, fn.month, fn.day)
        edad =relativedelta(datetime.now(), ini)
        tiempo = 'Edad: {0} año(s) y {1} mes(es)'.format(edad.years, edad.months)
        return txt.format(self.director, tiempo)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=40, help_text='Ingres el Titulo de la Pelicula')
    descripcion = models.TextField(max_length=1000, help_text='Ingrese breve descripción de la Pelicula')
    estreno = models.IntegerField(help_text='Fecha de Estreno de la Pelicula')
    director = models.ForeignKey(Directores, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='peliculas/imagenes', null=True)

    def __str__(self):
        txt= 'Pelicula :  {0}  ( Director: {1})'
        return txt.format(self.titulo, self.director)
