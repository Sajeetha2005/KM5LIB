from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def details(request):
    return render(request, 'details.html')

def create(request):
    return render(request, 'create.html')

def author(request):
    return render(request, 'author.html')