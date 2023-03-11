from django.db import models
from django.contrib.auth.models import User


# Use to define user type in UserProfileModel

USER_TYPE = (
    (0, "I'm a financial advisor"),
    (1, "I'm looking for advice")
)


class Location(models.Model):

    """
    location model: stores all the specialisation types available.
    They are equal to the advice seeker need.
    """

    city = models.CharField(max_length=30)

    def __str__(self):
        """Change display value of specialisation"""
        return self.city


class Specialisation(models.Model):

    """
    Specialisations model: stores all the specialisation types available.
    They are equal to the advice seeker need.
    """

    type = models.CharField(max_length=30)

    def __str__(self):
        """Change display value of specialisation"""
        return self.type


class UserProfile(models.Model):

    """
    UserProfile model: at signup auser is asked whether they are Advisors
    or Seekers and the asnwer is stored in this model. This is needed to decide
    what signup form to show next: the one for advisors or the one for seekers.
    If this model is undefined for a user, this step will alsways appear first 
    when someone logs in to the app again.
    """

    user_type = models.IntegerField(choices=USER_TYPE, blank=False, null=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profiles'
    )

    def __str__(self):

        """Change display value of userProfile"""

        l_name = self.user.last_name
        f_name = self.user.first_name

        return f'{f_name} {l_name} | {self.user_type}'
