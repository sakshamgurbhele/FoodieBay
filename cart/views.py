from django.shortcuts import render, get_object_or_404
from .cart import Cart
from FoodieBay.models import fooditem
from django.http import JsonResponse

# Create your views here.

def cart(request):
    cart = Cart(request)
    cart_total = cart.__len__()
    cart_products = cart.get_prods
    return render(request, 'cart.html', {"cart_products": cart_products, "cart_total": cart_total})

def cart_add(request):
#     #get the cart
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        # product_id = int(request.POST.get('product_id'))
        print(request.POST)  # Debugging: Log the received POST data
        product_id = request.POST.get("product_id")
        if not product_id:
            return JsonResponse({"error": "Product ID is missing"}, status=400)

        try:
            product_id = int(product_id)  # Ensure valid conversion
        except ValueError:
            return JsonResponse({"error": "Invalid Product ID"}, status=400)
    
        #lookup product in DB
        product = get_object_or_404(fooditem, id=product_id)
        #save to cart
        cart.add(product=product)
        
        #quantity 
        cart_quantity = cart.__len__()
        
        #return response
        response = JsonResponse({'qty': cart_quantity})
        return response
        
     # If not POST or action invalid, return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_delete(request):
    return 

def cart_update(request):
    return 