from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    allsigns = {'signs'}
    return render(request, '/styles/home.html', allsigns)