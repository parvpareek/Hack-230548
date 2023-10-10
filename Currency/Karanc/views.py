from django.shortcuts import render
import requests

def index(request):
    return render(request, 'Karanc/index.html')

# def exchange_rate(request):  Our currency processing funcitons here
#   return render(request,'Karnac')

