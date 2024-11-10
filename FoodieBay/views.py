from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def login(request):
    return render(request, 'login.html')
    
def register(request):
    return render(request, 'register.html')
    
def cart(request):
    return render(request, 'cart.html')
    

