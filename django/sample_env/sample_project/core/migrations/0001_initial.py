# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(default=b'leitor', max_length=50, verbose_name=b'Nome')),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('login', models.CharField(max_length=50, verbose_name=b'Login')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('about', models.TextField(max_length=500, verbose_name=b'Sobre')),
            ],
        ),
    ]