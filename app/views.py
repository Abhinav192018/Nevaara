from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Products(request):
    return render(request, 'Products.html')

def Clearance_sale(request):
    return render(request, 'clearance.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Contact(request):
    return render(request, 'contact.html')
