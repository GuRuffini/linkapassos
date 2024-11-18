from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cnpj',
        'email',
        'cidade',
        'estado',
        'telefone',
        'celular',
    )  
    search_fields = ('nome', 'cnpj', 'cidade', 'email')
    list_filter = ('cidade', 'estado')
    readonly_fields = ('cnpj',)
    list_editable = ('telefone', 'celular',)
    ordering = ('nome',)
    list_per_page = 20
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cnpj', 'email', 'site')
        }),
        ('Endereço', {
            'fields': ('cep', 'endereco', 'numero', 'bairro', 'cidade', 'estado')
        }),
        ('Contato', {
            'fields': ('telefone', 'celular')
        }),
    )
