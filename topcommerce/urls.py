"""topcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import urls as products_urls
from accounts import urls as accounts_urls
from shortlist import urls as shortlist_urls
from checkout import urls as checkout_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(products_urls)),
    path('accounts/', include(accounts_urls)),
    path('shortlist/', include(shortlist_urls)),
    path('checkout/', include(checkout_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
