from django.contrib import admin
from .models import Producto, TipoProducto, Marca

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre_producto", "marca", "stock", "precio", "tipo_producto"]
    list_editable = ["marca","stock", "precio"]
    search_fields = ["nombre_producto"]
    list_filter = ["marca", "nuevo", "tipo_producto"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto)
admin.site.register(Marca)

