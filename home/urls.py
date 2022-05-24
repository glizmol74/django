from django.urls import path
from .views import  home, detalle_director, peliculasCine

app_name= 'home'

urlpatterns =[
    path('', home, name='home'),
    path('director/<int:dir_id>', detalle_director, name='director'),
    path('peliculas/', peliculasCine, name='peliculas'),
]