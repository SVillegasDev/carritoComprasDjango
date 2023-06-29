from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from app.carro import Carro
from .models import Producto, TipoProducto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

# from .carro import Carro


def inicio(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'index.html', data)


def agregar_producto(request):

    data = {
        'form': ProductoForm
    }

    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
            return redirect(to=listar_producto)
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)


def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get("page", 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'producto/listar.html', data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == "POST":
        formulario = ProductoForm(
            data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to=listar_producto)
        else:
            data["form"] = formulario

    return render(request, 'producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="inicio")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)


def agregarProductoCarro(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("inicio")

def agregarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("carrito")

def eliminarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("carrito")

def restarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect("carrito")

def limpiarCarro(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("carrito")

def comprar(request):
    productos = Producto.objects.all()
    tipo = TipoProducto.objects.all()
    data={'productos': productos}    
    return render(request, 'comprar.html', data)
    










