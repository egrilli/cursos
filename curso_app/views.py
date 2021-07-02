from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django.contrib import messages
from curso_app.models import *

def index(request):
    context = {
        'cursos': Curso.objects.all()
    }
    return render(request, 'index.html', context)


def agregarLibro(request):

    if request.method == "POST":
        print(request.POST)
        errors= Curso.objects.validador_basico(request.POST)
        errors.update(Descripcion.objects.validador_basico(request.POST))

        if len(errors) > 0 :
            for key , value in errors.items():
                messages.error(request, value)
            
            request.session['curso_name'] = request.POST['name']
            request.session['curso_description'] = request.POST['description']

        else:
            print(request.POST)

            nuevo_curso = Curso.objects.create(name=request.POST['name']) 
            nueva_descripcion = Descripcion.objects.create(description=request.POST['description'], curso=nuevo_curso)

            messages.success(request, f" El curso {nuevo_curso.name} fue agregado")

            request.session['curso_name'] = ""
            request.session['curso_description'] = ""

    return redirect("/")


