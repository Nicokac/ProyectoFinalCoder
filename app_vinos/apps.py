from django.apps import AppConfig


class AppVinosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_vinos'

    def ready(self):
        import app_vinos.signals  # Importa las señales aquí