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
    return(render(request, 'bootstrap.html', context))

def white_table(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table-striped table-bordered"
    context['style'] = r'body { background: rgb(61, 58, 58) !important;} .carousel-inner > .carousel-item > img {width: 100%; ;} table{background-color: white;border-width: 5px !important; td{border-width: 5px;border-color: black !important;}}'
    return(render(request, 'bootstrap.html', context))

def search(request):
    query = request.GET.get('search')
    context = {}
    if query != '':
        context = {'info':Posts.objects.all().filter(username=query)}
    else:
        context["info"] = {'name':'ERROR','title':'Nothing found','body':'empty search request'}
    context['borders'] = "table table-dark table-striped"
    return (render(request, 'bootstrap.html', context))