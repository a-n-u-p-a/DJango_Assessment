from django.shortcuts import render

# Create your views here.

def check_data(request):
    return render(request, "home.html")