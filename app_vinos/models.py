from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Relación OneToOne con el modelo User
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.user.username})'
    
    @property
    def es_administrador(self):
        return self.user.is_staff  # Verifica si el usuario tiene estado de staff

    @property
    def es_cliente(self):
        return not self.user.is_staff  # Cliente si no es staff

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Mis usuarios'
        ordering = ('nombre',)

class Preferencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #El parámetro on_delete=models.CASCADE especifica que si se elimina un Usuario, todas sus Preferencias asociadas también serán eliminadas.
    sabor = models.CharField(max_length=100)
    intensidad = models.IntegerField()

    def __str__(self):
        return f'{self.usuario} {self.sabor} ({self.intensidad})'
    
class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    intensidad = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Alcohol by Volume (%)')
    ph = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='pH')
    ta = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Total Acidity (g/L)')
    rs = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name='Residual Sugar (g/L)')
    imagen = models.ImageField(upload_to='vinos', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.tipo} {self.sabor} {self.intensidad} {self.abv} {self.ph} {self.ta} {self.rs}' 
    
    class Meta():

        verbose_name = 'Vinos'
        verbose_name_plural = 'Mis vinos'
        ordering = ('nombre',)
    
class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    preferencia = models.ForeignKey(Preferencia, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f'Cata de {self.usuario} el {self.fecha} - Tipo: {self.get_tipo_de_cata_display()}'
    
class Cata(models.Model):

    tipo_cata = [('Blanco', 'Cata de Vinos Blancos'),
                 ('Tinto', 'Cata de Vinos Tintos'),
                 ('Online', 'Cata Online'),
                 ('Empresa', 'Cata para empresas')
                 ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    vinos = models.ManyToManyField(Vino)
    tipo_de_cata = models.CharField(max_length=20, choices=tipo_cata, default='Blanco')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f'Cata de {self.usuario} el {self.fecha}'
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    
    
      