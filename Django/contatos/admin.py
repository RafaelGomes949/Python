from django.contrib import admin

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome',
                    'telefone', 'data_criacao', 'mostrar')
    list_display_links = ('id', 'nome')
#    list_filter = ('nome')
    list_per_page = 10
    search_fields = ('id', 'nome')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
