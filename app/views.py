from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def oculto(request):
    return render(request, 'app/oculto.html')

def oculto2(request):
    return render(request, 'app/oculto2.html')