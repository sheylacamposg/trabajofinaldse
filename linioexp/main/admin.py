from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Localizacion, Producto, Categoria, Proveedor

# Register your models here.
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)