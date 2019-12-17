from django.contrib import admin
from .models import Post
from .models import Alumno
from .models import Materia
from .models import Profesor


admin.site.register(Post)

admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Profesor)