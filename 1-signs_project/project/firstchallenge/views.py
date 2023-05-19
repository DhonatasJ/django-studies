from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 

signs = {
    "aries": "March 21 - April 19",
    "taurus": "April 20 - May 20",
    "gemini": "May 21 - June 20",
    "cancer": "June 21 - July 22",
    "leo": "July 23 - August 22",
    "virgo": "August 23 - September 22",
    "libra": "October 23 - November 21",
    "sagittarius": "November 22 - December 21",
    "capricorn": "December 22 - January 19",
    "aquarius": "January 20 - February 18",
    "pisces": "February 19 - March 20",
}


def monthly_challenge_number(request, month):
    signKey = list(signs.keys())
    foward_key = signKey[month]
    return HttpResponseRedirect('signs/' + foward_key)

def home(request):
    list_items = ""
    for sign in signs:
        list_items += f"<li><a href='{sign}'>{sign.capitalize()}</a></li>"
    return HttpResponse(list_items)
    

def monthly_challenge(request, month):
    try:
        change_text = signs[month]
        respose_data = F"<h1>SIGN {change_text}</h1>"
    except:
        return HttpResponseNotFound(f'<p style="color: red; text-align: center; font-size: 24px;">SIGN NOT FOUND</p>')
    return HttpResponse(respose_data)




