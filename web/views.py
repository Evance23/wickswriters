from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render( request, "web/index.html")

def signup(request):
    return render(request, "web/signup.html")

def signin(request):
    return render(request, "web/signin.html")

def signout(request):
    pass