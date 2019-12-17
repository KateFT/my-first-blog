from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('lista_alumnos', views.alumnos, name='lista_alumnos'),
    path ('materias', views.vista_materias, name='materias'),
    path ('profesores', views.vista_profesores, name='profesores')
]