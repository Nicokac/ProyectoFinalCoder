from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Usuario, Preferencia, Vino, Recomendacion, Avatar, Cata
from .forms import UsuarioFormulario, VinosFormulario, UserEditForm, AvatarFormulario, CataForm, CustomUserCreationForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.
@login_required
def inicio(req):
    try:
        # Obtener la última cata agendada por el usuario logueado
        cata = Cata.objects.filter(usuario=req.user.usuario).last()
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {'url': avatar.imagen.url, 'cata': cata})
    except Avatar.DoesNotExist:
        # Si no tiene avatar, pero sí una cata
        cata = Cata.objects.filter(usuario=req.user.usuario).last()
        return render(req, "inicio.html", {'cata': cata})
    except:
        # Si ocurre otro error, retornar sin avatar ni cata
        return render(req, "inicio.html", {})

def crea_usuario(req, nombre, apellido, email):

    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
    nuevo_usuario.save()

    return HttpResponse(f"""<p> Nombre: {nuevo_usuario.nombre} - Apellido: {nuevo_usuario.apellido} - Email: {nuevo_usuario.email} creado con exito! </p>""")

@login_required
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

def eliminar_usuario(req, id):

    if req.method == 'POST':
        
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
    
        lista = Usuario.objects.all()

        return render(req, "lista_usuarios.html", {"lista_usuarios": lista})
    
def editar_usuario(req, id):
    
    usuario = Usuario.objects.get(id=id)

    if req.method == 'POST':

        mi_formulario = UsuarioFormulario(req.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.email = data['email']
            usuario.save()

            return HttpResponseRedirect('/app_vinos')
        
        else:
            return render(req, "usuario_formulario.html", {"mi_formulario": mi_formulario})

    else:

        mi_formulario = UsuarioFormulario(initial={
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "email": usuario.email,
        }) 
        return render(req, "editar_usuario.html", {"mi_formulario": mi_formulario, "id": usuario.id})

def vino_formulario(req):

    print('method', req.method)
    print('data', req.POST)

    if req.method == 'POST':

        mi_formulario = VinosFormulario(req.POST)

        print(mi_formulario)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data 

            nuevo_vino = Vino(nombre=data['nombre'], tipo=data['tipo'], sabor=data['sabor'], intensidad=data['intensidad'], abv=data['abv'], ph=data['ph'], ta=data['ta'], rs=data['rs'])
            nuevo_vino.save()

            #return render(req, "inicio.html", {})
            return HttpResponseRedirect('/app_vinos')
    
        else:
           
            return render(req, "vino_formulario.html", {"mi_formulario": mi_formulario}) 

    else:

        mi_formulario = VinosFormulario() 
        return render(req, "vino_formulario.html", {"mi_formulario": mi_formulario})

def mostrar_preferencias(req):

    return render(req, "preferencias.html", {})

def mostrar_recomendaciones(req):

    return render(req, "recomendaciones.html", {})

class VinoList(LoginRequiredMixin, ListView):

    model = Vino
    template_name = 'vino_list.html'
    context_object_name = 'vinos'

class VinoDetails(DetailView):

    model = Vino
    template_name = 'vino_details.html'
    context_object_name = 'vinos'

class VinoCreate(CreateView):

    model = Vino
    template_name = 'vino_create.html'
    #fields = ['nombre', 'tipo', 'sabor', 'intensidad', 'abv', 'ph', 'ta', 'rs']
    fields = ('__all__')
    success_url = '/app_vinos'

class VinoUpdate(UpdateView):

    model = Vino
    template_name = 'vino_update.html'
    fields = ('__all__')
    success_url = '/app_vinos'
    context_object_name = 'vinos'

class VinoDelete(DeleteView):

    model = Vino
    template_name = 'vino_delete.html'
    success_url = '/app_vinos'
    context_object_name = 'vinos'

def login_view(req):

    if req.method == 'POST':
        
        mi_formulario = AuthenticationForm(req, data=req.POST)
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render (req, "inicio.html", { "mensaje": f'Bienvenido {usuario}'})
            else:
                return render(req, "inicio.html", { "mensaje": f'Datos incorrectos'})

        else:
            return render(req, "login.html", { "mi_formulario": mi_formulario})
        
    else:
        mi_formulario = AuthenticationForm()
        return render(req, "login.html", { "mi_formulario": mi_formulario})

def register(req):
    if req.method == 'POST':
        mi_formulario = CustomUserCreationForm(req.POST)
        if mi_formulario.is_valid():
            user = mi_formulario.save(commit=False)
            user.first_name = mi_formulario.cleaned_data['first_name']
            user.last_name = mi_formulario.cleaned_data['last_name']
            user.email = mi_formulario.cleaned_data['email']
            user.save()

            # Verificar si ya existe un registro en el modelo Usuario para este User
            try:
                usuario, created = Usuario.objects.get_or_create(
                    user=user,
                    defaults={
                        'nombre': user.first_name,
                        'apellido': user.last_name,
                        'email': user.email
                    }
                )

                if not created:
                    # Si ya existía el registro, podemos actualizar los datos si es necesario
                    usuario.nombre = user.first_name
                    usuario.apellido = user.last_name
                    usuario.email = user.email
                    usuario.save()

            except IntegrityError:
                return render(req, "inicio.html", {"mensaje": "Error: el usuario ya existe."})

            return render(req, "inicio.html", { "mensaje": f'Usuario {user.username} creado exitosamente'})

        else:
            return render(req, "registro.html", { "mi_formulario": mi_formulario})

    else:
        mi_formulario = CustomUserCreationForm()
        return render(req, "registro.html", { "mi_formulario": mi_formulario})

@login_required
def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        mi_formulario = UserEditForm(req.POST, instance = req.user)
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", { "mensaje": f'Datos actualizados exitosamente'})
        
        else:
            return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario})
        
    else:

        mi_formulario = UserEditForm(instance = req.user)
        return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario})
    
def agregar_avatar(req):

    if req.method == 'POST':

        mi_formulario = AvatarFormulario(req.POST, req.FILES)
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()

            return render(req, "inicio.html", { "mensaje": f'Avatar creado correctamente'})
        
        else:
            return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario})
    
    else:

        mi_formulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario})

@login_required
def agendar_cata(req):
    if req.method == 'POST':
        mi_formulario = CataForm(req.POST)
        if mi_formulario.is_valid():
            cata = mi_formulario.save(commit=False)
            try:
                # Asignar el usuario actual logueado utilizando la relación OneToOne
                cata.usuario = req.user.usuario  # Aquí se asigna el usuario correcto
            except Usuario.DoesNotExist:
                return render(req, "inicio.html", {"mensaje": "Usuario no encontrado. Por favor, regístrate en el sistema."})
            cata.save()
            mi_formulario.save_m2m()  # Guardar la relación ManyToMany (vinos seleccionados)
            #return redirect('DetalleCata', cata_id=cata.id)
            return render(req, "inicio.html", {"mensaje": "La cata ha sido agendada correctamente"})
    else:
        mi_formulario = CataForm()

    return render(req, "agendar_cata.html", {"mi_formulario": mi_formulario})

@login_required
def detalle_cata(req):
    # Obtener todas las catas del usuario actual
    catas = Cata.objects.filter(usuario=req.user.usuario)

    # Pasar todas las catas al template
    return render(req, "detalle_cata.html", {'catas': catas})

def verificar_relacion_usuario(req):
    usuarios = Usuario.objects.select_related('user').all()  # Carga todos los usuarios
    resultado = []

    for user in User.objects.all():
        try:
            usuario = user.usuario
            resultado.append(f'User ID: {user.id}, Usuario ID: {usuario.id}, Nombre: {user.first_name}, Apellido: {user.last_name}, Email: {user.email}')
        except Usuario.DoesNotExist:
            resultado.append(f'User {user.username} no tiene un perfil de Usuario asociado.')

    return render(req, "verificar_relacion.html", {"usuarios": usuarios, "resultado": resultado})

def vista_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    
    if usuario.es_administrador:
        return HttpResponse("Este usuario es un administrador")
    elif usuario.es_cliente:
        return HttpResponse("Este usuario es un cliente")
