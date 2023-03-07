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
        on_delete=models.PROTECT,
        related_name='Advisors'
    )

    seeker = models.OneToOneField(
        SeekerUserProfile,
        on_delete=models.CASCADE,
        related_name='Seekers'
    )

    matched_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Change display value of User profile"""
        return f'{self.advisor} | {self.seeker}'


class Message(models.Model):

    """
    A message can only have one match. One match
    can have many messages.
    """

    match = models.ForeignKey(
        Match, on_delete=models.CASCADE,
        related_name='match'
        )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='sender'
        )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Message by {self.user}"
