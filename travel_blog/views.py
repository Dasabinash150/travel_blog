# Create your views here.
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    # return HttpResponse("index")
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def aboutus(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")
    # return HttpResponse("Hello world111!")
def single_blog(request):
    return render(request, "single_blogpost.html")
    # return HttpResponse("Hello world111!")

def contact(request):
    return render(request, "contact.html")

def imagegallery(request):
    return render(request, "image-gallery.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

    