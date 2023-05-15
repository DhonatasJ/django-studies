from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("firstchallenge/", include("firstchallenge.urls")),
    path("admin/", admin.site.urls),
]