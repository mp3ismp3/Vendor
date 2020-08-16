from django import forms
from .models import Vendor, Item
from django.utils.translation import gettext_lazy as _
class VendorModelForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels ={
            'vendor_name' : _('電商名稱'),
            'vendor_content' : _('內容'),
            'vendor_phone' : _('客服電話'),
            'vendor_addr' : _('商店位置'),
        }
class RawVendorForm(forms.Form):
    vendor_name = forms.CharField()
    vendor_content = forms.CharField()
    vendor_phone = forms.CharField()
    vendor_addr = forms.CharField()