from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm


def checkout(request):

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MQVNNC4VwW0IzXj93A03LIFFiBSGp5IpdVGpaCgzDTfZh7InRUYlrsB8jDqUoFy3RSawHFVYbpD6Hq5a4ubSzjo00GNiwRgLD',
        'client_secret': 'test client secret'
    }

    return render(request, 'checkout/checkout.html', context)
