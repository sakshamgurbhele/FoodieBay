from django.shortcuts import render, HttpResponse, redirect
from .models import fooditem, Contact, Order
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from cart.cart import Cart
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


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
    return render(request, 'register.html')
    
def checkout(request):
    cart = Cart(request)  # Initialize the cart
    cart_products = cart.cart  # Get all items in the cart
    cart_total = cart.get_total()  # Calculate the total price

    # Ensure the cart is not empty
    if not cart_products:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    # Prepare items data for the JSONField
    items_data = [
        {
            'product_id': int(product_id),
            'product_name': fooditem.objects.get(id=int(product_id)).item_name,
            'price': str(fooditem.objects.get(id=int(product_id)).price),
            'quantity': quantity,
        }
        for product_id, quantity in cart_products.items()
    ]

    # Save the order to the database
    new_order = Order.objects.create(
        items=items_data,
        total_price=cart_total
    )

    # Clear the cart after successful order placement
    cart.cart.clear()  # Clear the cart dictionary
    request.session['session_key'] = {}  # Clear session cart
    request.session.modified = True

    # Redirect to the order confirmation page with the new order ID
    return redirect('order_confirmation', order_id=new_order.order_id)
    

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})
  
 
def dashboard(request):
    order = Order.objects.all()
    return render(request, 'dashboard.html', {'orders': order})

    

