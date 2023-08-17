from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'DJmiddleware/index.html', {'ip_address': ip})


def Exp(request):
    return HttpResponse("Exception page:", 10/0)


def name(request):
    return render(request, 'DJmiddleware/name.html', {'name': 'yash'})
