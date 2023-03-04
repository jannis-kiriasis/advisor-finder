from django.conf import settings
from django.core.mail import send_mail


def define_context(order):
    """
    Define the variables to use in all the emails' contexts
    """
    context = {
        'seeker': f'{order.seeker.user.first_nam} \
                    {order.seeker.user.first_name}',
        'advisor': order.consultation.match.advisor.business_name,
        'date': order.consultation.date,
        'time': order.consultation.time,
        'fee': order.af_feeconsultation.price,
        'link': order.consultation.link,
        'order': order
    }

    return context


def consultation_confirmed_email(order):
    """
    Send email to advisor with details of the consultation confirmed.
    """
    context = define_context(order)

    subject = f'Consultation confirmed'
    message = render_to_string('emails/consultation-confirmed.txt', context)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.consultation.match.advisor.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def payment_failed_email(order):

    """
    Send email to seeker when order payment fails.
    """

    context = define_context(order)

    subject = f'Order payment failed | Advice Found'
    message = render_to_string('emails/payment-failed.txt', context)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def payment_succeeded_email(order):

    """
    Send email to seeker with details of the payment confirmed 
    and meeting details.
    """

    context = define_context(order)

    subject = f'Consultation confirmed'
    message = render_to_string(
        'emails/consultation-confirmed-seeker.txt',
        context
        )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.seeker.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
