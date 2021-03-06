# Generated by Django 4.0.4 on 2022-05-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_peliculas_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='descripcion',
            field=models.TextField(help_text='Ingrese breve descripción de la Pelicula', max_length=1000),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='estreno',
            field=models.IntegerField(help_text='Fecha de Estreno de la Pelicula'),
        ),
    ]
