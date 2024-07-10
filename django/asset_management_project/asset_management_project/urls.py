"""
URL configuration for asset_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# asset_management_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from assets import views as assets_views


router = DefaultRouter()
router.register(r'items', assets_views.ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', assets_views.catalog_view, name='catalog.html'),
    path('accounts/', include('django.contrib.auth.urls')),  # Django authentication URLs
    path('accounts/register/', assets_views.register_view, name='register'),  # Custom registration view
    path('accounts/profile/', assets_views.profile_view, name='profile'),
    path('api/', include(router.urls)),  # Custom profile view
    # Add other URL patterns as needed
]
