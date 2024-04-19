# Create your views here.
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse("Hello world!")
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    # return HttpResponse("index")