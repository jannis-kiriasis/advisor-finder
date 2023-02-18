from django.db import models
from django.contrib.auth.models import User
from home.models import Specialisation, Location
from .emails import send_approval_email

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

    def save(self):

        """
        Send email when approved is updated.
        """

        # Check whether the choice value has been changed when saving.
        # Send emails accordingly to the choice value.
        if self.id:

            old_approved_choice = AdvisorUserProfile.objects.get(pk=self.id)

            if old_approved_choice.approved == 0 and self.approved == 1:

                send_approval_email(self, 'approved. Now you can logit at https://advisor-finder.herokuapp.com/advisors/login/')

            elif old_approved_choice.approved == 0 and self.approved == 2:

                send_approval_email(self, 'not approved. Please review your profile at https://advisor-finder.herokuapp.com/accounts/login/ or email jannis.kiriasis@gmail.com to learn more.')

        super(AdvisorUserProfile, self).save()

    def __str__(self):
        """Change display value of User profile"""
        return self.business_name
