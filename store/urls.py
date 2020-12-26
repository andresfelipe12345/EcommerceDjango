from django.urls import path
#from . import views
from .views import store_cart_view, store_checkout_view, store_main_view

urlpatterns = [
    path('', store_main_view, name='store'),
    path('cart/', store_cart_view, name='cart'),
    path('checkout/', store_checkout_view, name='checkout'),
]
