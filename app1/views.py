from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Auto, Producto, Album
from app1.forms import AutoFormulario, ProductoFormulario, AlbumFormulario, AutoBusquedaFormulario, AlbumBusquedaFormulario, ProductoBusquedaFormulario


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

            # return render(request, "app1/auto_formulario.html")
            return redirect(listar_autos)
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

            # return render(request, "app1/producto_formulario.html")
            return redirect(listar_productos)
            
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

            # return render(request, "app1/album_formulario.html")
            return redirect(listar_albumes)
    else:
        albumformulario = AlbumFormulario()
    return render (request, "app1/album_formulario.html", {"albumformulario":albumformulario})


def index(request):

    return render(request, "app1/index.html")






def buscar_autos(request):
    
    busqueda_formulario = AutoBusquedaFormulario()

    if request.GET:    
     busqueda_formulario = AutoBusquedaFormulario(request.GET)
    if busqueda_formulario.is_valid():
            autos = Auto.objects.filter(modelo=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "app1/auto_busqueda.html", {"busqueda_formulario": busqueda_formulario, "autos": autos})


    return render(request, "app1/auto_busqueda.html", {"busqueda_formulario": busqueda_formulario})

def buscar_productos(request):
    
    busqueda_formulario_p = ProductoBusquedaFormulario()

    if request.GET:    
     busqueda_formulario_p = ProductoBusquedaFormulario(request.GET)
    if busqueda_formulario_p.is_valid():
            productos = Producto.objects.filter(nombre=busqueda_formulario_p.cleaned_data.get("criterio")).all()
            return render(request, "app1/producto_busqueda.html", {"busqueda_formulario_p": busqueda_formulario_p, "productos": productos})


    return render(request, "app1/producto_busqueda.html", {"busqueda_formulario_p": busqueda_formulario_p})

def buscar_albums(request):
    
    busqueda_formulario_a = AlbumBusquedaFormulario()

    if request.GET:    
     busqueda_formulario_a = AlbumBusquedaFormulario(request.GET)
    if busqueda_formulario_a.is_valid():
            albums = Album.objects.filter(nombre=busqueda_formulario_a.cleaned_data.get("criterio")).all()
            return render(request, "app1/album_busqueda.html", {"busqueda_formulario_a": busqueda_formulario_a, "albums": albums})


    return render(request, "app1/album_busqueda.html", {"busqueda_formulario_a": busqueda_formulario_a})