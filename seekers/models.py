from django.db import models
from django.contrib.auth.models import User
from home.models import Specialisation, Location


class SeekerUserProfile(models.Model):

    """
    SeekerUserProfile model: stores seeker information
    that aren't in User model. A SeekerUserProfile belongs only to one user.
    One user can only have one user profile.
    """

    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='seekers'
    )

    postcode = models.CharField(max_length=12, null=True, blank=True)

    town_or_city = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='address'
    )

    street_address = models.CharField(max_length=30, null=True, blank=True)

    need = models.ForeignKey(
        Specialisation,
        on_delete=models.PROTECT,
        related_name='needs'
    )

    def __str__(self):

        """
        Change display value of seeker profile
        """
        return f'{self.user.first_name} {self.user.last_name}'
