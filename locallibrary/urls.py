"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls import include
from django.views.generic.base import TemplateView
# from catalog import views as catalog_views
from django.contrib.auth import views
from .views import register

urlpatterns = [
    # path('account/',include(auth.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('vendor/', include('vendor.urls'), name = 'vendor'),
    path('', include('searchengine.urls')),
    path('home/', TemplateView.as_view(template_name ='registration/home.html'), name ='home'),
    path('register/', register, name = 'register'),
    # re_path(r'^new_add/(\d+)/(\d+)/$', catalog_views.add2, name = 'add2'),
    # re_path(r'^add/(\d+)/(\d+)/$', catalog_views.add, name ='add'),
]
