def order_paid(order):
    if order.paid is False:
        order.paid = True
        order.save()
