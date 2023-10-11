from django.shortcuts import render, redirect
import requests
from .user import *
from Karanc.protocols import *
from .agent import *

def index(request):
     return render(request, 'Karanc/index.html')