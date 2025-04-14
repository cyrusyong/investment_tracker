from django.urls import path, include
from django.contrib import admin

from plaidapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plaid/', include('plaidapp.urls')),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
]

