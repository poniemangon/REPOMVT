"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import (buscar_albums, formulario_albumes, formulario_autos, formulario_productos, listar_autos, listar_albumes, listar_productos, index, buscar_autos, buscar_productos)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carform/', formulario_autos),
    path('carlist/', listar_autos),
    path('productform/', formulario_productos),
    path('productlist/', listar_productos),
    path('albumform/', formulario_albumes),
    path('albumlist/', listar_albumes),
    path('index/', index),
    path('carfind/', buscar_autos),
    path('productfind/', buscar_productos),
    path('albumfind/', buscar_albums)

    
    
    
   

]
