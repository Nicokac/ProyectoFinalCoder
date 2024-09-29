from django.contrib import admin
from .models import Usuario, Vino, Preferencia, Recomendacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Vino)
admin.site.register(Preferencia)
admin.site.register(Recomendacion)

