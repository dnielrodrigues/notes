# coding: utf-8
from django.db import models


"""
--------------------------------------------------------------------------------
Classe Usuarios ...
--------------------------------------------------------------------------------
"""
class SampleUsers(models.Model):


    """
    campos ...
    ----------------------------------------------------------------------------
    """
    rule = models.CharField(max_length=50, default='leitor', verbose_name='Nome')
    name = models.CharField(max_length=50, verbose_name='Nome')
    login = models.CharField(max_length=50, verbose_name='Login')
    email = models.EmailField(verbose_name='Email')
    about = models.TextField(max_length=500, verbose_name='Sobre')


    """
    ????????
    ----------------------------------------------------------------------------
    """
    def __str__(self):
        return self.name


    """
    ???????? ...
    ----------------------------------------------------------------------------
    """
    # class Meta
    # verbose_name='Usuário'
    # verbose_name_plural='Usuários'
