from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse("Dates of signs")

def aries (request):
    return HttpResponse("Aries—March 21-April 19.")

def taurus (request):
    return HttpResponse("Taurus—April 20-May 20.")

def gemini (request):
    return HttpResponse("Gemini—May 21-June 20.")

def monthly_challenge(request, month):
    change_text = None
    if month == 'aries':
        change_text = 'Aries—March 21-April 19.'
    return HttpResponse








# def cancer(request):
#     return HttpResponse("Cancer—June 21-July 22.")

# def leo (request):
#     return HttpResponse("Leo—July 23-August 22.")

# def virgo (request):
#     return HttpResponse("Virgo—August 23-September 22.")

# def libra (request):
#     return HttpResponse("Libra—September 23-October 22.")

# def scorpio (request):
#     return HttpResponse("Scorpio—October 23-November 21.")

# def sagittarius (request):
#     return HttpResponse("Sagittarius—November 22-December 21.")

# def capricorn (request):
#     return HttpResponse("Capricorn—December 22-January 19.")

# def aquarius (request):
#     return HttpResponse("Aquarius—Jan 20-Feb 18.")

# def pisces (request):
#     return HttpResponse("Pisces—Feb 19-March 20.")

