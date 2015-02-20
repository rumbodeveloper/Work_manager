
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'en/public/index.html')

def connection(request):
    return render(request, 'en/public/connection.html')