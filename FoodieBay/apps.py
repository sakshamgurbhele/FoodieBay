# pylint: disable=bad-indentation,trailing-whitespace
""" Apps.py Define"""
from django.apps import AppConfig

class FoodiebayConfig(AppConfig):
    """Configuration class for Foodiebay application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FoodieBay'
