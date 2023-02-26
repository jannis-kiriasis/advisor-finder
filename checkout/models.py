import uuid

from django.db import models
from django.db.models import Sum
from seekers.models import SeekerUserProfile
from consultations.models import Consultation


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    consultation = models.OneToOneField(
        Consultation, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='consultation'
    )
    seeker = models.ForeignKey(
        SeekerUserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='seeker'
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):

        """
        Generate a random, unique order number using UUID
        """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):

        """
        Override the original save method to set the order number
        if it hasn't been set already and
        add Advice Found fee to the grand total.
        """

        af_fee = self.price * 5 / 100
        self.grand_total = self.price + af_fee

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number