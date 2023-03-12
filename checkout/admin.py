from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    Order admin panel. Decleare all fields to be available and 
    all the fields that are read only.
    """
    readonly_fields = ('order_number', 'date', 'grand_total',)
    fields = (
        'order_number', 'seeker', 'consultation', 'date',
        'name', 'last_name', 'email', 'phone_number',
        'postcode', 'town_or_city', 'street_address', 'fee',
        'af_fee', 'grand_total', 'stripe_pid', 'paid'
        )

    list_display = ('order_number', 'date', 'name', 'last_name',
                    'grand_total', 'paid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
