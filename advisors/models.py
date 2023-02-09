from django.db import models


STATUS = ((0, 'Not approved'), (1, 'Approved'))
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
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    town_or_city = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='locations'
    )

    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)

    specialisation = models.ForeignKey(
        Specialisation,
        on_delete=models.CASCADE,
        related_name='specialisations'
    )

    status = models.IntegerField(choices=STATUS, default=0)
    active = models.IntegerField(choices=ACTIVE, default=1)

    def __str__(self):
        """Change display value of User profile"""
        l_name = self.user.last_name
        f_name = self.user.first_name
        return f"{f_name} {l_name}"


class Specialisations(models.Model):

    """
    Specialisations model: stores all the specialisation types available.
    They are equal to the advice seeker need.
    """

    type = models.CharField(max_length=30)

    def __str__(self):
        """Change display value of specialisation"""
        return self.type


class Location(models.Model):

    """
    location model: stores all the specialisation types available.
    They are equal to the advice seeker need.
    """

    city = models.CharField(max_length=30)

    def __str__(self):
        """Change display value of specialisation"""
        return self.city
