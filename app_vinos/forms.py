from django import forms

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class VinosFormulario(forms.Form):

    nombre = forms.CharField() 
    tipo = forms.CharField()
    sabor = forms.CharField()
    intensidad = forms.CharField()
    abv = forms.DecimalField()
    ph = forms.DecimalField()
    ta = forms.DecimalField()
    rs = forms.DecimalField()  