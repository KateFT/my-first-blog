from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Alumno (models.Model):
    nombre = models.CharField(max_length=50)
    apellidom = models.CharField(max_length=100)
    apellidop = models.CharField(max_length=100)

class Profesor (models.Model):
    nombre=models.CharField(max_length=50)
    materia=models.ForeignKey('Materia', on_delete=models.CASCADE)

class Materia(models.Model):
    nombre=models.CharField(max_length=50)
