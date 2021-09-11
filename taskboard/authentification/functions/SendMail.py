from django.core.mail import send_mail
from django.conf import settings

class SendMail:
    def __init__(self,text,recipient_list):
        self.text = text
        self.recipient_list = recipient_list
    def send(self):
        subject = 'Devu Build'
        send_mail( subject, self.text, settings.EMAIL_HOST_USER, self.recipient_list )