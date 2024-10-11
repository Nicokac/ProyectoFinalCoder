from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario

@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        # Crear el objeto Usuario asociado al User recién creado
        Usuario.objects.create(user=instance, email=instance.email, nombre=instance.first_name, apellido=instance.last_name)
