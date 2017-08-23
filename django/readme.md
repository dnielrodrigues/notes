# Comandos Básicos

- Install Django
```pip install django```

- Iniciar projeto
```django-admin startproject project_name```

- Criar app (modulo do django)
```python manage.py startapp project_name module_name```

- Adicionar o app (modulo) criado no settings.py
```
INSTALLED_APPS=[
  ...
  'module_name'
]
```

- Iniciar aplicacao
```python manage.py runserver```

- Criar primeiro usuário
```python manage.py createsuperuser```


# Conectar ao PostgreSQL

- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

# Sincronizar com banco legado

- https://docs.djangoproject.com/pt-br/1.11/howto/legacy-databases/
