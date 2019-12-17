from django.shortcuts import render
from .models import Alumno, Materia, Profesor


def post_list(request):
	return render (request, 'blog/post_list.html', {}) 

def alumnos(request):
	alumnos=Alumno.objects.order_by('apellidop')
	materias=Materia.objects.all()
	profesores=Profesor.objects.all()
	return render (request,'blog/alumnos.html', {'alumnos':alumnos, 'materias':materias, 'profesores':profesores})

def vista_materias(request):
	materias=Materia.objects.all()
	return render (request, 'blog/alumnos.html',{'materias':materias})

def vista_profesores(request):
	profesores=Profesor.objects.all()
	return render (request, 'blog/alumnos.html',{'profesores':profesores})
