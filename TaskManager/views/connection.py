
# Create your views here.
from django.shortcuts import render

def page(request):
    return render(request, 'en/public/connection.html')

