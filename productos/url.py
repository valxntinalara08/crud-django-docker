from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.producto_detalle),
]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]

urlpatterns = [
    # URL raíz → redirige a lista
    path('', views.inicio, name='inicio'),


    # Listado de todos los productos
    path('productos/', views.lista_productos, name='lista_productos'),


    # Crear nuevo producto
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),


    # Ver detalle de un producto (pk = ID numérico en la URL)
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),


    # Editar un producto
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),


    # Eliminar un producto
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]