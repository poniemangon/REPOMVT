from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Auto
from app1.forms import AutoFormulario


# Create your views here.

def listar_autos(request):
    context = {}
    context["autos"] = Auto.objects.all()

    return render(request, "app1/lista_autos.html", context)


def formulario_autos(request):
  
    if request.method == "POST":

        mi_formulario = AutoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data


            car = Auto(marca=informacion['marca'], modelo=informacion['modelo'])
            car.save()

            return render(request, "app1/auto_formulario.html")
    else:
        mi_formulario = AutoFormulario()
    return render (request, "app1/auto_formulario.html", {"mi_formulario":mi_formulario})