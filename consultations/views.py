# from django.shortcuts import render
# from .forms import ConsultationForm
# from .models import Consultation
# from matches.models import Match


# def create_consultation(request, match):

#     """
#     """
#     form = ConsultationForm(data=request.POST)

#     if form.is_valid():

#         form.instance.match = match
#         form.save()

#         # Email consultation to seeker

#         # Get all consultations by logged in user
#         consultations = Consultation.objects.filter(user=request.user)

#         # Get last message for logged in user by created_on and send
#         consultation = consultations.latest('created_on')
#         # email_consultation_to_seeker(consultation)

#         messages.success(
#             request,
#             'Consultation created. An email has been sent to your client.'
#             )

#     else:

#         form = ConsultationForm()

