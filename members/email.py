from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import requests

def check_email_existence(email):
    api_key = '498396a888e7f9bc2fb07092fb7615d724b15bd9'
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']['result'] == 'deliverable':
            return True
        else:
            return False
    else:
        return False


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
