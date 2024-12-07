# pylint: disable=bad-indentation,trailing-whitespace,missing-final-newline
"""Context processor for cart functionality."""
from .cart import Cart

def cart(request):
   """Return cart instance for template context."""
   return {'cart': Cart(request)}