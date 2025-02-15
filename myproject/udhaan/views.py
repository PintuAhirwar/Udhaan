from django.shortcuts import render
from django.http import HttpResponse
# from .models import product
from math import ceil
# from .models import User
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'site/index.html')