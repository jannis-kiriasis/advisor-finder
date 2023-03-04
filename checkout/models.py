import uuid

from django.db import models
from django.db.models import Sum
from seekers.models import SeekerUserProfile
from consultations.models import Consultation
from consultations.services import confirm_consultation
from home.models import Location


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
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    street_address = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    af_fee = models.DecimalField(max_digits=5, decimal_places=2)
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

        self.fee = self.consultation.price or 0
        self.af_fee = self.fee * 5 / 100
        self.grand_total = self.fee + self.af_fee

        if not self.order_number:
            self.order_number = self._generate_order_number()

        order = self
        confirm_consultation(order)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
