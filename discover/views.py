from django.shortcuts import render

def index(request):
    return render(request, 'discover/index.html')

def entreprises(request):
    return render(request, 'discover/entreprises.html')

def freelances(request):
    return render(request, 'discover/freelances.html')

def histoire(request):
    return render(request, 'discover/histoire.html')