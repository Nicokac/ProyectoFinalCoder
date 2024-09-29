from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Usuario, Preferencia, Vino, Recomendacion
from .forms import UsuarioFormulario

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

def usuario_formulario(req):

    print('method', req.method)
    print('data', req.POST)

    if req.method == 'POST':

        mi_formulario = UsuarioFormulario(req.POST)

        print(mi_formulario)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data 

            nuevo_usuario = Usuario(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            nuevo_usuario.save()

            return render(req, "inicio.html", {})
    
        else:
           
            return render(req, "usuario_formulario.html", {"mi_formulario": mi_formulario}) 

    else:

        mi_formulario = UsuarioFormulario() 
        return render(req, "usuario_formulario.html", {"mi_formulario": mi_formulario})
    
def busqueda_usuario(req):

    return render(req, "busqueda_usuario.html")

def buscar_usuario(req):

    # Capturar el término de búsqueda de la URL
    termino_busqueda = req.GET.get("termino")
    #nombre_usuario = req.GET["nombre"]

    #nombre = Usuario.objects.get(nombre=nombre_usuario)
    #nombre = Usuario.objects.filter(nombre=nombre_usuario)

        # Usar Q para buscar por nombre, apellido o email
    usuarios = Usuario.objects.filter(
        Q(nombre__icontains=termino_busqueda) |
        Q(apellido__icontains=termino_busqueda) |
        Q(email__icontains=termino_busqueda)
    )

    return render(req, "resultado_busqueda.html", {"termino": termino_busqueda, "usuarios": usuarios})
    #return render(req, "resultado_busqueda.html", {"nombre": nombre_usuario, "apellido": nombre})

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