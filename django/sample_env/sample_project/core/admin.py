# coding: utf-8
from django.contrib import admin

# importando models ...
from models import SampleUsers
from models import Pages


"""
registrando modulos ...
--------------------------------------------------------------------------------
"""
admin.site.register(SampleUsers)
admin.site.register(Pages)