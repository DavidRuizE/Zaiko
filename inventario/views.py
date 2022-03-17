from ssl import HAS_TLSv1_1
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

from .models import producto

def home(request):
    return render(request, 'home.html')



def inv(request):
    searchTerm= request.GET.get('buscarProducto')
    if searchTerm:
        Productos = producto.objects.filter(title__icontains=searchTerm)
    else:
        Productos=producto.objects.all()
    return render(request, 'inv.html', {'searchTerm':searchTerm, 'Productos':Productos})

def about(request):
    return HttpResponse('<h1> Welcome to about page</h1>')


# Create your views here.
