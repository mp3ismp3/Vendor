from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 20)
    vendor_content = models.CharField(max_length = 500)
    vendor_phone = models.CharField(max_length = 10)
    vendor_addr = models.CharField(max_length = 30)
    #vendor_found = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.vendor_name
    def get_absolute_url(self):
        return reverse('vendors:vendor_id', kwargs={'pk' : self.id})

class Item(models.Model):
    item_name = models.CharField(max_length = 20)
    item_content = models.CharField(max_length = 500)
    item_price = models.DecimalField(max_digits = 6, decimal_places = 0)
    item_vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name

class Morethanthou(admin.SimpleListFilter):
    title = _('price')
    parameter_name = 'compareprice'

    def lookups(self, request, model_admin):
        return(
            ('>1000',_('價格大於1000')),
            ('<=1000',_('價格落在0-1000')),
        )
    def queryset(self, request, queryset):
        if self.value() == '>1000':
            return queryset.filter(item_name__gt=1000)
        if self.value() == '<=1000':
            return queryset.filter(item_name__lte=1000)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_name', 'vendor_phone', 'vendor_addr')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
    list_filter = (Morethanthou,)
    fields = ['item_price']
    search_fields = ['item_name', 'item_price']
    ordering = ['-item_price']

        