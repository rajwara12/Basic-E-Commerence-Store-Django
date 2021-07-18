from django.urls import path
from . import views
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('order/', views.order, name="order"),
    path('checkout', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    
]