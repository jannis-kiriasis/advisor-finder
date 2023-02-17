from .forms import AdvisorSignupForm
from .models import AdvisorUserProfile, User
from django.conf import settings
from django.core.mail import send_mail
from .advisors import views


def advisor_to_approve_email(user, profile):

    """
    Email AdviceFound when profile is submitted after signup or edit.
    """

    subject = 'Advisor Profile to review'
    message = f'A new profile {profile.business_name} has been sent for review. Login to the admin panel to review and approve it.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_deactivated_email(user, profile):

    """
    Email user when profile is deactivated.
    """

    subject = 'Advisor Profile deactivated'
    message = f'Dear {profile.business_name}, your profile has been deactivated. You will be hidden from AdviceFound and will not be able to receive new leads.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_activated_email(user, profile):

    """
    Email user when profile is activated.
    """

    subject = 'Advisor Profile activated'
    message = f'Dear {profile.business_name}, your profile has been activated. You are now able to receive new leads.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, email_from, recipient_list)
