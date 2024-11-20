from django.shortcuts import render, get_object_or_404
from .cart import Cart
from FoodieBay.models import fooditem
from django.http import JsonResponse

# Create your views here.

def cart(request):
    cart = Cart(request)
    cart_total = cart.__len__()
    quantity = cart.get_quants()
    cart_products = cart.get_prods
    totals = cart.get_total
    # Assume quantity.items is a dictionary with product_id as keys and quantity as values

    # Pass a range of 1-10 to the template for quantities
    # context = {
    #     'cart_products': cart_products,
    #     'quantity': quantity,
    #     'quantity_range': list(range(1, 11))  # Pass the range here
    # }
    return render(request, 'cart.html', {"cart_products": cart_products, "cart_total": cart_total, "quantity":quantity, "totals":totals})

def cart_add(request):
#     #get the cart
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        # product_id = int(request.POST.get('product_id'))
        print(request.POST)  # Debugging: Log the received POST data
        product_id = request.POST.get("product_id")
        product_qty = request.POST.get("product_qty")
        if not product_id:
            return JsonResponse({"error": "Product ID is missing"}, status=400)

        try:
            product_id = int(product_id)  # Ensure valid conversion
        except ValueError:
            return JsonResponse({"error": "Invalid Product ID"}, status=400)
    
        #lookup product in DB
        product = get_object_or_404(fooditem, id=product_id)
        
        #save to cart
        cart.add(product=product, quantity=product_qty)
        
        #quantity 
        cart_quantity = cart.__len__()
        
        #return response
        response = JsonResponse({'qty': cart_quantity})
        return response
        
     # If not POST or action invalid, return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get("product_id")
        #call delete function
        cart.delete(product=product_id)
        #return response
        response = JsonResponse({'product': product_id})
        return response

def cart_update(request):
    return 