# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sampleusers',
            options={'verbose_name': 'Usu\xe1rio', 'verbose_name_plural': 'Usu\xe1rios'},
        ),
        migrations.AlterField(
            model_name='sampleusers',
            name='rule',
            field=models.CharField(default=b'leitor', max_length=50, verbose_name=b'Tipo de Usu\xc3\xa1rio'),
        ),
    ]
