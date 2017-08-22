# coding: utf-8
from django.shortcuts import render

# listar paginas ...
def list_pages(request):
    return render(request, 'pages/list_pages.html', {})
