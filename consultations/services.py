from django.shortcuts import get_object_or_404


def confirm_consultation(order):
    get_consultation = order.consultation

    get_consultation.status = 1
    get_consultation.save()
