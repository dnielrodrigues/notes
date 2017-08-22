# coding: utf-8
from django.db import models


"""
--------------------------------------------------------------------------------
Classe Usuarios ...
--------------------------------------------------------------------------------
"""
class SampleUsers(models.Model):

    # campos ...
    rule = models.CharField(max_length=50, default='leitor', verbose_name='Tipo de Usuário')
    name = models.CharField(max_length=50, verbose_name='Nome')
    login = models.CharField(max_length=50, verbose_name='Login')
    email = models.EmailField(verbose_name='Email')
    about = models.TextField(max_length=500, verbose_name='Sobre')

    # ??? ...
    def __str__(self):
        return self.name

    # forcando verbose automatico no django ...
    class Meta:
        verbose_name='Usuário'
        verbose_name_plural='Usuários'



"""
--------------------------------------------------------------------------------
Classe Paginas ...
--------------------------------------------------------------------------------
"""
class Pages(models.Model):

    # campos ...
    title = models.CharField(max_length=50, verbose_name='Título')
    content = models.TextField(verbose_name='Conteúdo da Página')

    # ??? ...
    def __str__(self):
        return self.title

    # forcando verbose automatico no django ...
    class Meta:
        verbose_name='Página'
        verbose_name_plural='Páginas'
