from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def inicio(request):
    return redirect('lista_productos')


def lista_productos(request):
    busqueda = request.GET.get('q', '')
    productos = Producto.objects.all()

    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda)
            | Q(categoria__icontains=busqueda)
            | Q(descripcion__icontains=busqueda)
        )

    context = {
        'productos': productos,
        'busqueda': busqueda,
        'total_productos': productos.count(),
    }
    return render(request, 'productos/lista_productos.html', context)


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/form_producto.html', {'form': form, 'titulo': 'Nuevo producto'})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/form_producto.html', {'form': form, 'titulo': 'Editar producto'})


def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminacion.html', {'producto': producto})
from django.http import HttpResponse

def producto_detalle(request, id):
    return HttpResponse(f"Producto número {id}")