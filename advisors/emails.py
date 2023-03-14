from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def advisor_to_approve_email():
    """
    Specifics of Advice Found email received when advisors signs up
    or edit their account.
    """
    subject = 'Advisor Profile to review'
    message = render_to_string(
        'advisors/emails/advisor-to-approve-email.txt')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_deactivated_email(profile):
    """
    Advisor account deactivated email.
    """
    subject = 'Advisor Profile deactivated'
    message = render_to_string(
        'advisors/emails/advisor-deactivated-email.txt',
        {'profile': profile})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [profile.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def advisor_activated_email(profile):
    """
    Advisor account activated email.
    """
    subject = 'Advisor Profile activated'
    message = render_to_string(
        'advisors/emails/advisor-activated-email.txt',
        {'profile': profile})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [profile.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def send_approval_email(self, is_approved):
    """
    Advisor approval email.
    """
    subject = 'Advisor profile approval update'
    message = render_to_string(
        'advisors/emails/send-approval-email.txt',
        {'self': self},
        {'is_approved': is_approved})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [self.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def email_note_to_seeker(last_message):
    """
    Seeker receives an email when advisor send a message.
    """
    subject = 'Advice Found: you have a new message'
    message = render_to_string(
        'advisors/emails/email-note-to-seeker.txt',
        {'last_message': last_message})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def consultation_cancelled(consultation):
    """
    Seeker receives an email when a consultation is cancelled.
    """
    subject = 'Advice Found: you have a new message'
    message = render_to_string(
        'advisors/emails/consultation-cancelled.txt',
        {'consultation': consultation})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [consultation.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
