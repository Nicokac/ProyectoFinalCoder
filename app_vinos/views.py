from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Preferencia, Vino, Recomendacion

# Create your views here.

def inicio(req):

    return render(req, "inicio.html", {})

def crea_usuario(req, nombre, apellido, email):

    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
    nuevo_usuario.save()

    return HttpResponse(f"""<p> Nombre: {nuevo_usuario.nombre} - Apellido: {nuevo_usuario.apellido} - Email: {nuevo_usuario.email} creado con exito! </p>""")

def lista_usuarios(req):

    lista = Usuario.objects.all()

    return render(req, "lista_usuarios.html", {"lista_usuarios": lista})

def cargar_vino(req, nombre, tipo, sabor, intensidad, abv, ph, ta, rs):

    nuevo_vino = Vino(nombre=nombre, tipo=tipo, sabor=sabor, intensidad=intensidad, abv=abv, ph=ph, ta=ta, rs=rs)
    nuevo_vino.save()

    return HttpResponse(f"""<p> Nombre: {nuevo_vino.nombre} - Tipo: {nuevo_vino.tipo} - Sabor: {nuevo_vino.sabor} 
                        - Intensidad: {nuevo_vino.intensidad} - ABV: {nuevo_vino.abv} - pH: {nuevo_vino.ph} - ta: {nuevo_vino.ta} - rs: {nuevo_vino.rs} cargado con exito! </p>""")

def lista_vinos(req):

    lista = Vino.objects.all()

    return render(req, "lista_vinos.html", {"lista_vinos": lista})

def mostrar_preferencias(req):

    return render(req, "preferencias.html", {})

def mostrar_recomendaciones(req):

    return render(req, "recomendaciones.html", {})