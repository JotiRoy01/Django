from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    #return HttpResponse("Hello, world => Home Page")
    return render(request, "website/index.html")
def about(request) :
    return HttpResponse("Hello, world => About Page")

def contact(request) :
    return HttpResponse("Hello, world => Contact Page")