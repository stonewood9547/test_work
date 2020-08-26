import json
import requests
from django.shortcuts import render
from .models import Posts, Users, Adress, Company
from django.core import exceptions

# Create your views here.

def index(request):
    context = {'info':Posts.get_data(self=Posts)}
    return(render(request, 'index.html', context))

def black_table(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table table-dark table-striped"
    return(render(request, 'black.html', context))

def white_table(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table-striped table-bordered"
    return(render(request, 'white.html', context))

def search(request):
    query = request.GET.get('search')
    try:
        data = {'info':Posts.objects.all().filter(username=query)}
    except:
        data = {}
    data['borders'] = "table table-dark table-striped"
    return (render(request, 'black.html', context=data))

def color_table(request):
    query = request.GET.get('color')
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = query
    return(render(request, 'white.html', context))