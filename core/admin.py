from django.contrib import admin
from .models import (Marca, Veiculo, Pessoa, Parametros, MovRotativo,
Mensalista, MovMensalista)

class MovRotativoAdim(admin.ModelAdmin):
    list_display = ('checkin', 'checkout',
     'valor_hora', 'veiculo', 'pago', 'total', 'veiculos')

    def veiculos(self, obj):
        return 'Ola'

class MovMensalistaAdim(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdim)
admin.site.register(MovRotativo, MovRotativoAdim)
