from django.urls import path
from . import views
app_name ='vendors'
urlpatterns=[
    # FBV
    # path('', views.vendor_index, name = 'index'),
    # path('<int:id>/',views.singleVendor, name ='vendor_id'),
    # path('create/', views.VendorCreateView, name = 'create'),
    # CBV
    path('create/', views.VendorCreateView.as_view(), name = 'create'),
    path('', views.VendorListView.as_view(), name = 'index'),
    path('<int:pk>/', views.VendorDetailView.as_view(), name = 'vendor_id'),
    path('<int:pk>/update/', views.VendorUpdateView.as_view(), name = 'update'),
]