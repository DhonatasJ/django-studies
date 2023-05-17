from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:month>/', views.monthly_challenge_number),
    path('<str:month>/', views.monthly_challenge, name="signs-challenge"),
]
