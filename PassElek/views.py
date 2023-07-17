from django.shortcuts import render
from django.views.generic import ListView

def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'hakimizda.html')


def iletsim(request):
    return render(request, 'iletsim.html')


def hizmetler(request):
    return render(request, 'hizmetler.html')



