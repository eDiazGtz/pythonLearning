from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('checkout/<int:orderId>', views.checkoutPage),
    path('new', views.new),
]
