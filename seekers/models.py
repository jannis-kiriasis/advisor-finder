from django.db import models
from django.contrib.auth.models import User
from home.models import Specialisation, Location

STATUS = ((0, 'Not approved'), (1, 'Approved'))
ACTIVE = ((0, 'Not active'), (1, 'Active'))


class SeekerUserProfile(models.Model):

    """
    SeekerUserProfile model: stores seeker information
    that aren't in User model. A SeekerUserProfile belongs only to one user.
    One user can only have one user profile.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='seekers'
    )

    postcode = models.CharField(max_length=20, null=True, blank=True)

    town_or_city = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='address'
    )

    street_address = models.CharField(max_length=80, null=False, blank=False)

    need = models.ForeignKey(
        Specialisation,
        on_delete=models.CASCADE,
        related_name='needs'
    )

    def __str__(self):

        """
        Change display value of seeker profile
        """
        return f'{self.user.first_name} {self.user.last_name}'
