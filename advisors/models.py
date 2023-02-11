from django.db import models
from django.contrib.auth.models import User
from home.models import Specialisation, Location

APPROVED = ((0, 'pending'), (1, 'approved'), (2, 'not approved'))
ACTIVE = ((0, 'Not active'), (1, 'Active'))


class AdvisorUserProfile(models.Model):

    """
    AdvisorUserProfile model: stores advisor information
    that aren't in User model. An AdvisorUserProfile belongs only to one user.
    One user can only have one user profile.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='users'
    )

    business_name = models.CharField(max_length=100)
    business_description = models.CharField(max_length=500)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    town_or_city = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='locations'
    )

    street_address = models.CharField(max_length=80, null=False, blank=False)

    specialisation = models.ForeignKey(
        Specialisation,
        on_delete=models.CASCADE,
        related_name='specialisations'
    )

    registration_number = models.CharField(max_length=100)
    approved = models.IntegerField(choices=APPROVED, default=0)
    active = models.IntegerField(choices=ACTIVE, default=1)

    def __str__(self):
        """Change display value of User profile"""
        return self.business_name
