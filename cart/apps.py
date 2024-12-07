# pylint: disable=bad-indentation,trailing-whitespace
"""Application configuration for cart module."""
from django.apps import AppConfig


class CartConfig(AppConfig):
    """Configuration class for cart application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
