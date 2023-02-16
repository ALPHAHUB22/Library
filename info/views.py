from django.shortcuts import render
# from rest_framework.response import Response
from django.http import HttpResponse, Http404, HttpRequest
from .forms import Register

# Create your views here.
def index(request):
    return render(request, "info/home.html")

def register(request):
    context = {"form":Register}
    return render(request, "info/register.html", context)

def login(request):
    return render(request,"info/login.html")