from django.shortcuts import render, get_object_or_404
from .models import Vendor
#from .forms import VendorForm
from .forms import RawVendorForm, VendorModelForm
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView

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

#-----------------------------------------------------------------------------------------
# CBV

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_lst.html'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendors/vendor_Detail2.html'
    
class VendorCreateView(CreateView):
    form_class = VendorModelForm
    # model = Vendor
    # fields = '__all__'
    template_name = 'vendors/vendor_create.html'

class VendorUpdateView(UpdateView):
    form_class = VendorModelForm
    template_name ='vendors/vendor_create.html'
    queryset = Vendor.objects.all()

#  class HomePageView(TemplateView):
#      template_name ='home.html'

# class ItemListView(ListView):
#     model = Item
#     template_name = 