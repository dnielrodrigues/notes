# Comandos Básicos

- Install Django
```pip install```

- Iniciar projeto
```django-admin startproject app_name```

- Criar app (modulo do django)
```python manage.py app_name module_name```

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
