from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'grand_total',)
    fields = ('order_number', 'seeker', 'consultation', 'date',
                'first_name', 'last_name', 'email', 'phone_number',
                'postcode', 'town_or_city',
                'street_address', 'fee', 'grand_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
