from django.contrib import admin
from .models import Usuario, Vino, Preferencia, Recomendacion, Avatar, Cata

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'apellido', 'email']
    search_fields = ['nombre', 'apellido']
    list_filter = ['nombre']

class VinoAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'tipo', 'sabor', 'intensidad', 'abv', 'ph', 'ta', 'rs']
    search_fields = ['nombre', 'tipo', 'sabor', 'intensidad', 'abv', 'ph', 'ta', 'rs']
    list_filter = ['nombre', 'tipo', 'sabor', 'intensidad', 'abv', 'ph', 'ta', 'rs']

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Vino, VinoAdmin)
admin.site.register(Preferencia)
admin.site.register(Recomendacion)
admin.site.register(Avatar)
admin.site.register(Cata)

