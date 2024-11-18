from django.db import models
from .validators import validate_cnpj

class Empresa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Empresa')
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cnpj],
        verbose_name='CNPJ'
    )
    site = models.URLField(max_length=200, blank=True, null=True, verbose_name='Site')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='Número')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    telefone = models.CharField(max_length=10, blank=True, null=True, verbose_name='Telefone Fixo')
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular')

    def __str__(self):
        return f'{self.nome} - {self.cnpj}'

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']
