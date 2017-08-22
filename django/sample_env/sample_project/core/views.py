# coding: utf-8
from django.shortcuts import render
from .models import Pages

# listar paginas ...
def list_pages(request):
    pages = Pages.objects.all()
    data = {'paginas':pages}

    return render(request, 'pages/list_pages.html', data)
