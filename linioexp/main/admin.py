from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, Colaborador, Profile

from .models import Localizacion, Producto, Categoria, Proveedor, Pedido, DetallePedido, Profile, Cliente, Colaborador
class ClienteInline(admin.TabularInline):
    model=Cliente

class ColaboradorInline(admin.TabularInline):
    model=Colaborador

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]
# Register your models here.
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Cliente)
admin.site.register(Colaborador)
