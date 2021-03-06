from django import forms


class AutoFormulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()


class AlbumFormulario(forms.Form):

    nombre = forms.CharField()
    banda = forms.CharField()
    year = forms.IntegerField()

class ProductoFormulario(forms.Form):

    nombre = forms.CharField()
    marca = forms.CharField()
    tipo = forms.CharField()
    precio = forms.IntegerField()

class AutoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()
class ProductoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()
class AlbumBusquedaFormulario(forms.Form):
    criterio = forms.CharField()


