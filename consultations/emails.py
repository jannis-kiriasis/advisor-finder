from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def email_consultation_seeker(consultation_form):

    """
    Send an email to the seeker with the Advisor schedule an appointment.
    """

    context = {
        'seeker': consultation_form.match.seeker.first_name,
        'advisor': consultation_form.match.advisor.business_name,
        'date': consultation_form.date,
        'time': consultation_form.time,
        'fee': consultation_form.price,
        'login': 'accounts/login.html'
    }

    subject = 'Advice Found: you have a new appointment request'
    message = render_to_string('emails/consultation-email.html', context)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
