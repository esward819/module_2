from django.contrib import admin
from django.urls import path
from app.views import hello_world, hello_world2

urlpatterns = [
    path('<name>/', hello_world, name="basecamp"),
    path('', hello_world2)
]
