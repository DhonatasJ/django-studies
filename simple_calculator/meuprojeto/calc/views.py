from django.shortcuts import render
from django.http import HttpResponse  

def home(request):
    return render(request, 'home.html', {'style': 'style.css'})

def add(request):
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))
    res = val1 + val2
    return HttpResponse(res)
