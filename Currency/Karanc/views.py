from django.shortcuts import render
import requests

def index(request):
    return render(request, 'Karanc/index.html')

def limit(request):
    # if request.method=="POST":
     return render(request, 'Karanc/limit.html')


