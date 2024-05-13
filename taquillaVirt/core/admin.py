from django.contrib import admin
from core.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'direccion', 'telefono', 'email')

admin.site.register(Cliente, ClienteAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('tipo_usuario', 'descripcion')

admin.site.register(Usuario, UsuarioAdmin)

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('numeracion', 'estado')
admin.site.register(Localidad, LocalidadAdmin)

class GradaAdmin(admin.ModelAdmin):
    list_display = ('nombre_grada', 'aforo')
admin.site.register(Grada, GradaAdmin)

class EspectaculoAdmin(admin.ModelAdmin):
    list_display = ('nombre_espectaculo', 'productor')
admin.site.register(Espectaculo, EspectaculoAdmin)

class RecintoAdmin(admin.ModelAdmin):
    list_display = ('nombre_recinto', 'direccion')
admin.site.register(Recinto, RecintoAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre_evento', 'fecha_evento', 'descripcion')

admin.site.register(Evento, EventoAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_reserva', 'metodo_pago', 'pago_efectuado')
admin.site.register(Reserva, ReservaAdmin)


admin.site.register(LocalidadesOfertadas)

