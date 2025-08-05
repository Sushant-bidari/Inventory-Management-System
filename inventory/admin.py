from django.contrib import admin
from .models import Stock, Supplier  # only import what exists here

admin.site.register(Stock)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'delivery_time', 'defect_rate', 'price')
    list_editable = ('delivery_time', 'defect_rate', 'price')
    search_fields = ('name', 'phone', 'email', 'gstin')
