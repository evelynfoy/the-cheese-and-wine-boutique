''' urls for the Cheese and Wine application '''
from django.contrib import admin
from django.urls import path, include
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
]

handler404 = 'cheese_wine_boutique.views.handler404'
