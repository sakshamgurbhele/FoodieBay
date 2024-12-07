# pylint: disable=bad-indentation,trailing-whitespace,missing-final-newline
"""Views for handling shopping cart operations."""
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from FoodieBay.models import fooditem
from .cart import Cart

def cart(request):
    """Render cart page with products and totals."""
    cart_obj = Cart(request)
    cart_total = len(cart_obj)
    quantity = cart_obj.get_quants()
    cart_products = cart_obj.get_prods
    totals = cart_obj.get_total
    return render(request, 'cart.html', {
       "cart_products": cart_products,
       "cart_total": cart_total,
       "quantity": quantity,
       "totals": totals
    })

def cart_add(request):
   """Add product to cart and return updated quantity."""
   cart_obj = Cart(request)
   if request.POST.get('action') == 'post':
       product_id = request.POST.get("product_id")
       product_qty = request.POST.get("product_qty")
       if not product_id:
           return JsonResponse({"error": "Product ID missing"}, status=400)
       try:
           product_id = int(product_id)
       except ValueError:
           return JsonResponse({"error": "Invalid Product ID"}, status=400)
       product = get_object_or_404(fooditem, id=product_id)
       cart_obj.add(product=product, quantity=product_qty)
       cart_quantity = len(cart_obj)
       return JsonResponse({'qty': cart_quantity})
   return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_delete(request):
   """Remove product from cart."""
   cart_obj = Cart(request)
   if request.POST.get('action') == 'post':
       product_id = request.POST.get("product_id")
       cart_obj.delete(product=product_id)
       return JsonResponse({'product': product_id})
   return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_update(request):
   """Update cart quantities."""
   return request