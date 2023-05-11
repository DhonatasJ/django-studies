from django.shortcuts import render
from .models import Destination

def index(request):
    destn = Destination()
    destn.name = "Nice Travel"

    dest1 = Destination()
    dest1.name = 'Mutuipe'
    dest1.img = 'news_1.jpg'
    dest1.price = 700.69
    dest1.offer = True



    dest2 = Destination()
    dest2.name = 'Jiquirica'
    dest2.img = 'news_2.jpg'
    dest2.price = 542.90
    dest2.offer = False


    dest3 = Destination()
    dest3.name = 'Valenca'
    dest3.img = 'news_3.jpg'
    dest3.price = 1345.45
    dest3.offer = True


    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests' : dests})
