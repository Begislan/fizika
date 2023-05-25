from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request, "jjj.html")

def core(request):
    core_glav = CoreGlav.objects.all()
    glav = Glav.objects.all()
    theme = Theme.objects.all()
    context = {
        'c_gl': core_glav,
        'glav': glav,
        'theme': theme
    }
    return render(request, "core.html", context)

def them(request, pk):
    theme = Theme.objects.all().filter(pk=pk)
    context = {
        'theme': theme
    }
    return render(request, "theme.html", context)