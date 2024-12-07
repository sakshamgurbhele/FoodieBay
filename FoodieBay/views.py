# pylint: disable=bad-indentation,no-member
"""Views for handling web application functionality."""
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from cart.cart import Cart
from .models import fooditem, Contact, Order

def home(request):
    """Render homepage with all food items."""
    fooditems = fooditem.objects.all()
    return render(request, 'index.html', {'fooditems': fooditems})

def about(request):
    """Render about page."""
    return render(request, 'about.html', {})

def product(request, pk):
    """Display individual product details."""
    item = fooditem.objects.get(id=pk)
    return render(request, 'product.html', {'product': item})

def contact(request):
    """Handle contact form submissions."""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('emailAddress')
        message = request.POST.get('message')
        contact_entry = Contact(name=name, email=email, message=message, date=datetime.today())
        contact_entry.save()
        messages.success(request, "Your Query was Register!")
    return render(request, 'contact.html')

def login_user(request):
    """Handle user login."""
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In!")
            return redirect('/')
        messages.success(request, "There was an error, try again :)")
        return redirect('/')
    return render(request, 'login_user.html')

def logout_user(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, "You have been sucessfully logged out!")
    return redirect('/')

def register(request):
    """Handle user registration."""
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create(email=email, username=username)
            user.set_password(password)
            user.save()
            return render(request, 'index.html')
        messages.success(request, "Your password didn't match")
        return render(request, 'index.html')
    return render(request, 'register.html')

def checkout(request):
    """Process checkout and create order."""
    cart = Cart(request)
    cart_products = cart.cart
    cart_total = cart.get_total()

    if not cart_products:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    items_data = [
        {
            'product_id': int(product_id),
            'product_name': fooditem.objects.get(id=int(product_id)).item_name,
            'price': str(fooditem.objects.get(id=int(product_id)).price),
            'quantity': quantity,
        }
        for product_id, quantity in cart_products.items()
    ]

    new_order = Order.objects.create(items=items_data, total_price=cart_total)
    cart.cart.clear()
    request.session['session_key'] = {}
    request.session.modified = True

    return redirect('order_confirmation', order_id=new_order.order_id)

def order_confirmation(request, order_id):
    """Display order confirmation."""
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})

def access_denied(request):
    """Display access denied page."""
    return render(request, 'access_denied.html')

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='access-denied/')
def dashboard(request):
    """Display admin dashboard."""
    orders = Order.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'dashboard.html', {'orders': orders, 'contacts': contacts})

def add_item(request):
    """Add new food item."""
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        non_veg = request.POST.get("non_veg") == "true"
        image = request.FILES.get("image")

        if not all([item_name, description, price]):
            return JsonResponse({"success": False, "error": "Missing fields"})

        new_item = fooditem.objects.create(
            item_name=item_name,
            description=description,
            price=price,
            image=image,
            non_veg=non_veg,
        )
        return JsonResponse({"success": True, "item_id": new_item.id})
    return JsonResponse({"success": False, "error": "Invalid request method"})

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='access-denied/')
def order_details(request):
    """Display order details."""
    orders = Order.objects.all()
    return render(request, 'order_details.html', {'orders': orders})

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='access-denied/')
def contact_queries(request):
    """Display contact queries."""
    contacts = Contact.objects.all()
    return render(request, 'contact_queries.html', {'contacts': contacts})

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='access-denied/')
def add_fooditem(request):
    """Display add food item form."""
    return render(request, 'add_fooditem.html')
