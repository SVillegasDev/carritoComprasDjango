
from django.contrib import admin
from django.urls import include, path
from app import views as v
from prueba3 import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", v.inicio, name="inicio"),  
    path('agregar-producto/', v.agregar_producto, name="agregar_producto"),
    path('listar-producto/', v.listar_producto, name="listar_productos"),
    path('modificar-producto/<id>/', v.modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', v.eliminar_producto, name="eliminar_producto"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', v.registro, name="registro"),
    path('agregarproducto/<int:producto_id>/', v.agregarProductoCarro, name="agregar"),
    path('agregar/<int:producto_id>/', v.agregarProducto, name="Add"),
    path('eliminar/<int:producto_id>/', v.eliminarProducto, name="Del"),
    path('restar/<int:producto_id>/', v.restarProducto, name="Sub"),
    path('limpiar/', v.limpiarCarro, name="CLS"),
    path('carrito/', v.comprar, name="carrito"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

