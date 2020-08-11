from django.urls import path
from . import views
app_name ='vendors'
urlpatterns=[
    path('', views.vendor_index, name = 'index'),
    path('create', views.vendor_create_view, name = 'create'),
    path('<int:id>/',views.singleVendor, name ='vendor_id'),
]