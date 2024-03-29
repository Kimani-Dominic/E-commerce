from django.urls import path
from . import views


urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("login/", views.LoginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("update-item/", views.UpdateItem, name="update-item"),
]
