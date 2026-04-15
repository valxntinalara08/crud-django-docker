from django.db import models

class Producto(models.Model):
    # Campos de datos — cada campo = una columna en la BD
    nombre      = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio      = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.PositiveIntegerField(default=0)
    categoria   = models.CharField(max_length=80)
    activo      = models.BooleanField(default=True)


    # Campos automáticos de auditoría
    fecha_creacion      = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['nombre']           # Ordena por nombre por defecto
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


    def __str__(self):
        return self.nombre              # Representación legible del objeto


