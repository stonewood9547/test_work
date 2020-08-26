import json
import requests
from django.shortcuts import render
from .models import Posts, Users, Adress, Company
from django.core import exceptions

# Create your views here.

def index(request):
    context = {'info':Posts.get_data(self=Posts)}
    return(render(request, 'index.html', context))

def test(request):
    context = {'info':Posts.get_data(self=Posts)}
    return(render(request, 'test.html', context))

def test1(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table-striped table-bordered"
    return(render(request, 'test1.html', context))


def search(request):
    query = request.GET.get('search')
    context = {'info':Posts.objects.get(username=query)}
    return (render(request, 'test.html', context))