from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'landing-page'),
    path('shop/', views.shop, name = 'shop-home'),
    path('shop/<int:id>/', views.shop, name = 'shop-home'),
    path('shop/<int:id>/<str:order>/', views.shop, name = 'shop-home'),
    path('shop/profile', views.profile, name = 'user-profile'),
    path('item/new', views.newItem, name = 'item-create'),
    path('register/', views.register, name = 'register'),
]