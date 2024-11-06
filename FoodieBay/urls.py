from django.contrib import admin
from django.urls import path
from FoodieBay import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('register/', views.register)
]
