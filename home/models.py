from django.db import models


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
