from django.contrib import admin
from .models import Producto




# @admin.register es un decorador que registra el Modelo
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que aparecen en la lista del admin
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'activo')


    # Campos por los que se puede buscar en la barra de búsqueda del admin
    search_fields = ('nombre', 'categoria')


    # Filtros en la barra lateral del admin
    list_filter = ('activo', 'categoria')

