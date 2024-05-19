from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_email(email, activation_code):
    subject = 'Активация вашей учетной записи'
    html_message = render_to_string('activation_email.html', {'activation_code': activation_code, 'email': email})
    plain_message = strip_tags(html_message)
    sender_email = 'pharmacyshopgpt@gmail.com'
    recipient_list = [email]

    send_mail(
        subject,
        plain_message,
        sender_email,
        recipient_list,
        fail_silently=False,
        html_message=html_message
    )
    print("send email!!!!")
