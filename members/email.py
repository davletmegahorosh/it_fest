from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_activation_email(email, activation_code):
    subject = 'Активация вашей учетной записи'
    message = render_to_string('activation_email.html', {'activation_code': activation_code})
    sender_email = 'pharmacyshopgpt@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, sender_email, recipient_list,  fail_silently=False)
    # send_mail(subject, message, from_email, recipient_list, fail_silently=False)

