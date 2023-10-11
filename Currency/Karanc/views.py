from django.shortcuts import render, redirect
import requests
from .user import *
from Karanc.protocols import *
from .agent import *

def index(request):
     return render(request, 'Karanc/index.html')

def limit(request):
     base_currency = request.GET.get('baseCurrency')
     foreign_currency = request.GET.get('foreignCurrency')
     runAgent()

     user.setParams(base_currency, foreign_currency)

     runUser()     


     return render(request, 'Karanc/limit.html')