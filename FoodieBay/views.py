from django.shortcuts import render, HttpResponse, redirect
from .models import fooditem, Contact
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    fooditems = fooditem.objects.all()
    return render(request, 'index.html', {'fooditems': fooditems})
    
def about(request):
    return render(request, 'about.html', {})
    
def product(request, pk):
    product = fooditem.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('emailAddress')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, ("Your Query was Register!"))
    return render(request, 'contact.html')
    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged In!!!"))
            return redirect('/')
        else:
            messages.success(request, ("There was an error, try again :)"))
            return redirect('/')
    else:
        return render(request, 'login_user.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been sucessfully logged out!"))
    return redirect('/')
    
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create(email=email, username=username, password=password)
            user.set_password(password)
            user.save()
            return render(request, 'index.html')
        else: 
            messages.success(request, ("Your password didn't match"))
            return render(request, 'index.html')
    
    

