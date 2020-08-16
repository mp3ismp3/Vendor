from django.urls import path, re_path
from . import views
app_name = 'searchengine'
urlpatterns = [
    path('', views.homeview, name = 'home'),
]
