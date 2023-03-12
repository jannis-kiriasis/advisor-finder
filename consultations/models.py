from django.db import models
from matches.models import Match
from django import forms
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.core.exceptions import ValidationError


CONFIRMED = ((0, 'Not confirmed'), (1, 'Confirmed'))


def validate_date(date):
    """
    Function to check if date input is a past date. If so, raise an error.
    """
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Consultation(models.Model):
    """
    A consultation has a 1 to many relation with a match. One match can have
    many consultations, one consultation can have one match only.
    """
    match = models.ForeignKey(
        Match, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='consultation'
        )

    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(validators=[validate_date])
    time = models.TimeField()
    link = models.CharField(max_length=30)
    status = models.IntegerField(choices=CONFIRMED, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        """
        On save, create a link for the meeting.
        """
        # Create meeting link with random string
        self.link = 'https://gotalk.to/' + get_random_string(length=10)
        super().save(*args, **kwargs)
