from django.db import models
from matches.models import Match


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

    link = models.CharField(max_length=20)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Consultation on {self.date} at {self.time}'
