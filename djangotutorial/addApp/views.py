from django.shortcuts import render

# Create your views here.
def my_firstApp(request) :
    return render(request, "all_firstApp.html")