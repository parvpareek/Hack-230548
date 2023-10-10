from django.shortcuts import render, redirect
import requests

def index(request):
     return render(request, 'Karanc/index.html')

def limit(request):
    base_currency = request.GET.get('baseCurrency')
    foreign_currency = request.GET.get('foreignCurrency')
    return redirect('another_function')



