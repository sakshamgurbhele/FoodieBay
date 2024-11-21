from django.contrib import admin
from django.urls import path
from FoodieBay import views

# app_name = 'FoodieBay'  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('register/', views.register, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<uuid:order_id>/', views.order_confirmation, name='order_confirmation'),
]
