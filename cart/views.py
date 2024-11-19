from django.shortcuts import render, get_object_or_404
from .cart import Cart
from FoodieBay.models import fooditem
from django.http import JsonResponse

# Create your views here.

def cart(request):
    return render(request, 'cart.html', {})

def cart_add(request):
    #get the cart
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #lookup product in DB
        product = get_object_or_404(fooditem, id=product_id)
        #save to cart
        cart.add(product=product)
        #return response
        response = JsonResponse({'Product Name: ': product.item_name})
        return response
        
     # If not POST or action invalid, return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_delete(request):
    return 

def cart_update(request):
    return 