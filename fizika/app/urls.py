from django.urls import path
from .views import core, them, base

urlpatterns = [
    
    path('', core, name="core"),
    path('theme/<int:pk>', them, name="theme")
]