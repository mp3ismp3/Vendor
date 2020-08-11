from django.shortcuts import render, get_object_or_404
from .models import Vendor
#from .forms import VendorForm
from .forms import RawVendorForm
from django.http import Http404
# from django.views.generic import ListView, DetailView

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all()  #vendor_list>>>list
    context = {'vendor_list': vendor_list}
    return render(request, 'vendors/vendor_detail.html', context)
# def vendor_create_view(request):
#     form = VendorForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = VendorForm
#     context = {
#          'form' : form
#     }
#     return render(request, 'vendors/vendor_create.html', context)
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data)
        form = RawVendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)
    

def singleVendor(request, id):
    vendor_one = get_object_or_404(Vendor, id=id)
    # try:
    #     vendor_one = Vendor.objects.get(id=id) # vendor_one>dict()
    # except Vendor.DoesNotExist:
    #     raise Http404
    context = {
        'vendor_one' : vendor_one
        }
    return render(request, "vendors/vendor_singleVendor.html", context)

# class VendorListView(ListView):
#     model = Vendor
#     template_name = 'vendors/vendor_detail.html'

# class VendorDetail(DetailView):
#     model = Vendor
#     template_name = 'vendors/vendor_vendor_singleVendor.html'

