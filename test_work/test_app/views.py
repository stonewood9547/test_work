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