from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def email_consultation_seeker(consultation):

    """
    Send an email to the seeker with the Advisor schedule an appointment.
    """

    context = {
        'seeker': consultation.match.seeker.user.first_name,
        'advisor': consultation.match.advisor.business_name,
        'date': consultation.date,
        'time': consultation.time,
        'fee': consultation.price,
        'login': 'accounts/login.html'
    }

    subject = 'Advice Found: you have a new appointment request'
    message = render_to_string('emails/consultation-email.txt', context)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [consultation.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
