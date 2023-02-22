from django.db import models
from django.contrib.auth.models import User
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile


class Match(models.Model):

    """
    Match model: store details about a match.
    """

    advisor = models.ForeignKey(
        AdvisorUserProfile,
        on_delete=models.CASCADE,
        related_name='Advisors'
    )

    seeker = models.ForeignKey(
        SeekerUserProfile,
        on_delete=models.CASCADE,
        related_name='Seekers'
    )

    matched_on = models.DateTimeField(auto_now_add=True)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        """Change display value of User profile"""
        return f'{self.advisor} | {self.seeker}'
