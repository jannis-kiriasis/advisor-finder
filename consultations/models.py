from django.db import models
from matches.models import Match
from django import forms


CONFIRMED = ((0, 'Not confirmed'), (1, 'Confirmed'))

class Consultation(models.Model):

    """
    A consultation has a 1 to many relation with a match. One match can have
    many consultations, one consultation can have one match only.
    """

    match = models.ForeignKey(
        Match, on_delete=models.CASCADE,
        related_name='consultation'
        )

    price = models.DecimalField(max_digits=5, decimal_places=2)

    date = models.DateField()
    time = models.TimeField()

    link = models.CharField(max_length=30)

    status = models.IntegerField(choices=CONFIRMED, default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
