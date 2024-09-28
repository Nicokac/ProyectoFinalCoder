from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Preferencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #El parámetro on_delete=models.CASCADE especifica que si se elimina un Usuario, todas sus Preferencias asociadas también serán eliminadas.
    sabor = models.CharField(max_length=100)
    intensidad = models.IntegerField()

    def __str__(self):
        return f'{self.sabor} ({self.intensidad})'
    
class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    intensidad = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Alcohol by Volume (%)')
    ph = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='pH')
    ta = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Total Acidity (g/L)')
    rs = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Residual Sugar (g/L)')

    def __str__(self):
        return self.nombre
    
class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    preferencia = models.ForeignKey(Preferencia, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f'Recomendación para {self.usuario.nombre} - {self.vino.nombre}'
    
    
    
      