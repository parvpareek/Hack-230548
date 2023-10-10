from django.shortcuts import render
import requests

def index(request):
     return render(request, 'Karanc/index.html')

def limit(request):
    base_currency = request.GET.get('baseCurrency')
    foreign_currency = request.GET.get('foreignCurrency')

    # Do something with the variables in your view logic

    return render(request, 'Karanc/limit.html')
    # if request.method=="POST":


