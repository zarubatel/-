from django.http import HttpResponse
from django.shortcuts import render

def f_page(request):
    a = '<h1>Helllo world</h1>'
    text  = 'самый новый текст'
    return render(request, './index.html', {'a':a, 'text':text})
