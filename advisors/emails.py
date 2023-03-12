from django.conf import settings
from django.core.mail import send_mail


def advisor_to_approve_email(profile):

    """
    Specifics of Advice Found email received when advisors signs up
    or edit their account.
    """

    subject = 'Advisor Profile to review'
    message = f'A new profile {profile.business_name} has been sent for review. Login to the admin panel to review and approve it.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_deactivated_email(profile):
    """
    Specifics of Advisor account deactivated email.
    """
    subject = 'Advisor Profile deactivated'
    message = f'Dear {profile.business_name}, \
        your profile has been deactivated. \
        You will be hidden from AdviceFound. \
        and will not be able to receive new leads.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [profile.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_activated_email(profile):

    """
    Specifics of Advisor account activated email.
    """

    subject = 'Advisor Profile activated'
    message = f'Dear {profile.business_name}, your profile has been activated. You are now able to receive new leads.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [profile.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def send_approval_email(self, is_approved):

    """
    Specifics of Advisor approval email.
    """

    subject = 'Advisor profile approval update'
    message = f'The advisor profile for {self.business_name} has been {is_approved}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [self.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def email_note_to_seeker(last_message):

    """
    Advisor receives an email when seeker send a message.
    """

    subject = 'Advice Found: you have a new message'
    message = f'From: {last_message.user.users.business_name}. Message: {last_message.body}. Sent on {last_message.created_on}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def consultation_cancelled():

    """
    Advisor receives an email when seeker send a message.
    """

    subject = 'Advice Found: you have a new message'
    message = f'From: {last_message.user.users.business_name}. Message: {last_message.body}. Sent on {last_message.created_on}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)