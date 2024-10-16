from django.urls import path 
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('crear_usuario/<nombre>/<apellido>/<email>', crea_usuario),
    #path('cargar_vino/<nombre>/<tipo>/<sabor>/<intensidad>/<abv>/<ph>/<ta>/<rs>', cargar_vino),
    path('cargar_vino/', vino_formulario, name="CargaVino"),
    path('lista_usuarios/', lista_usuarios, name="ListaUsuarios"),
    #path('lista_vinos/', lista_vinos, name="ListaVinos"),
    path('recomendaciones/', mostrar_recomendaciones, name="MostrarRecomendaciones"),
    path('preferencias/', mostrar_preferencias, name="MostrarPreferencias"),
    path('usuario-formulario/', usuario_formulario, name="UsuarioFormulario"),
    path('busqueda-usuario/', busqueda_usuario, name="BusquedaUsuario"),
    path('buscar-usuario/', buscar_usuario, name="BuscarUsuario"),
    path('eliminar-usuario/<int:id>', eliminar_usuario, name="EliminarUsuario"),
    path('editar-usuario/<int:id>', editar_usuario, name="EditarUsuario"),

    path('vino_lista/', VinoList.as_view(), name="VinoLista"),
    path('vino_detalles/<pk>', VinoDetails.as_view(), name="VinoDetalles"),
    path('vino_crear/', VinoCreate.as_view(), name="VinoCrear"),
    path('vino_editar/<pk>', VinoUpdate.as_view(), name="VinoEditar"),
    path('vino_borrar/<pk>', VinoDelete.as_view(), name="VinoBorrar"),

    path('login/', login_view, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name="Logout"),

    path('editar-perfil/', editar_perfil, name="EditarPerfil"),

    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),

    path('agendar_cata/', agendar_cata, name='AgendarCata'),

    path('detalle_cata/', detalle_cata, name='DetalleCata'),

    path('verificar_relacion/', verificar_relacion_usuario, name='VerificarRelacion'),

    path('todas_las_catas/', ver_todas_las_catas, name='TodasLasCatas'),
    path('eliminar_cata/<int:cata_id>/', eliminar_cata, name='EliminarCata'),
    path('descriptivo_tipos_cata/', descriptivo_tipos_cata, name='DescriptivoTiposCata'),
]
