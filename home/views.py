from django.shortcuts import render, get_object_or_404
from .models import Directores, Peliculas

def home(request):
    director = Directores.objects.all()
    return render(request, 'home.html', {'Directores': director})

def detalle_director(request, dir_id):
    Director = get_object_or_404(Directores, pk=dir_id)
    peliculas = Peliculas.objects.filter(director=dir_id)
    #peliculas = get_object_or_404(Peliculas, director=dir_id)
    return render(request, 'detalle_pelicula.html', {'Peliculas': peliculas, 'Director': Director})

def peliculasCine(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {'Peliculas': peliculas})
