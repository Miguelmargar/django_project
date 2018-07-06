from .views import login, register_buyer, register_seller, logout, profile
from django.urls import path


urlpatterns = [
    path('login/', login, name="login"),
    path('register/buyer', register_buyer, name="register_buyer"),
    path('register/seller', register_seller, name="register_seller"),
    path('logout/', logout, name="logout"),
    path('profile/', profile, name="profile"),
    ]