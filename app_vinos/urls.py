from django.urls import path
from .views import inicio, crea_usuario, cargar_vino ,lista_usuarios, lista_vinos, mostrar_preferencias, mostrar_recomendaciones, usuario_formulario, busqueda_usuario, buscar_usuario

urlpatterns = [
    path('', inicio),
    path('crear_usuario/<nombre>/<apellido>/<email>', crea_usuario),
    path('cargar_vino/<nombre>/<tipo>/<sabor>/<intensidad>/<abv>/<ph>/<ta>/<rs>', cargar_vino),
    path('lista_usuarios/', lista_usuarios, name="ListaUsuarios"),
    path('lista_vinos/', lista_vinos, name="ListaVinos"),
    path('recomendaciones/', mostrar_recomendaciones, name="MostrarRecomendaciones"),
    path('preferencias/', mostrar_preferencias, name="MostrarPreferencias"),
    path('usuario-formulario/', usuario_formulario, name="UsuarioFormulario"),
    path('busqueda-usuario/', busqueda_usuario, name="BusquedaUsuario"),
    path('buscar-usuario/', buscar_usuario, name="BuscarUsuario"),

]
