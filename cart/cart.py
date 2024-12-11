# pylint: disable=bad-indentation,trailing-whitespace,E1101,missing-final-newline 
"""Shopping cart implementation with session handling."""
from FoodieBay.models import fooditem

class Cart:
   """Class to manage shopping cart operations using session storage."""
   
   def __init__(self, request):
       """Initialize cart with session data."""
       self.session = request.session
       cart = self.session.get('session_key')
       if 'session_key' not in request.session:
           cart = self.session['session_key'] = {}
       self.cart = cart

   def add(self, product, quantity):
       """Add or update product quantity in cart."""
       product_id = str(product.id)
       product_qty = int(quantity)
       self.cart[product_id] = int(product_qty)
       self.session.modified = True

   def __len__(self):
       """Return total number of items in cart."""
       return len(self.cart)

   def get_prods(self):
       """Get all products in cart from database."""
       product_ids = self.cart.keys()
       products = fooditem.objects.filter(id__in=product_ids)
       return products

   def get_quants(self):
       """Return quantities of items in cart."""
       return self.cart

   def delete(self, product):
       """Remove product from cart."""
       product_id = str(product)
       if product_id in self.cart:
           del self.cart[product_id]
       self.session.modified = True

   def get_total(self):
       """Calculate total price of items in cart."""
       product_ids = self.cart.keys()
       products = fooditem.objects.filter(id__in=product_ids)
       quantities = self.cart
       total = 0
       for key, value in quantities.items():
           key = int(key)
           for product in products:
               if product.id == key:
                   total = total + (product.price * value)
       self.session.modified = True
       return total
      