from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Auto, Producto, Album
from app1.forms import AutoFormulario, ProductoFormulario, AlbumFormulario


# Create your views here.

def listar_autos(request):
    context = {}
    context["autos"] = Auto.objects.all()

    return render(request, "app1/lista_autos.html", context)

def listar_productos(request):
    context = {}
    context["productos"] = Producto.objects.all()

    return render(request, "app1/lista_productos.html", context)

def listar_albumes(request):
    context = {}
    context["albumes"] = Album.objects.all()

    return render(request, "app1/lista_albumes.html", context)


def formulario_autos(request):
  
    if request.method == "POST":

        carformulario = AutoFormulario(request.POST)
        print(carformulario)
        if carformulario.is_valid:

            informacion = carformulario.cleaned_data


            car = Auto(marca=informacion['marca'], modelo=informacion['modelo'])
            car.save()

            return render(request, "app1/auto_formulario.html")
    else:
        carformulario = AutoFormulario()
    return render (request, "app1/auto_formulario.html", {"carformulario":carformulario})


def formulario_productos(request):
  
    if request.method == "POST":

        productoformulario = ProductoFormulario(request.POST)
        print(productoformulario)
        if productoformulario.is_valid:

            informacion = productoformulario.cleaned_data


            producto = Producto(nombre=informacion['nombre'], marca=informacion['marca'], tipo=informacion['tipo'],precio=informacion['precio'])
            producto.save()

            return render(request, "app1/producto_formulario.html")
    else:
        productoformulario = ProductoFormulario()
    return render (request, "app1/producto_formulario.html", {"productoformulario":productoformulario})


def formulario_albumes(request):
  
    if request.method == "POST":

        albumformulario = AlbumFormulario(request.POST)
        print(albumformulario)
        if albumformulario.is_valid:

            informacion = albumformulario.cleaned_data


            album = Album(nombre=informacion['nombre'], banda=informacion['banda'], year=informacion['year'])
            album.save()

            return render(request, "app1/album_formulario.html")
    else:
        albumformulario = AlbumFormulario()
    return render (request, "app1/album_formulario.html", {"albumformulario":albumformulario})


