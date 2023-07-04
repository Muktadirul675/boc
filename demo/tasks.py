from celery import shared_task
import time
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from boc import settings


@shared_task
def handle_sleep():
    print("Handle sleep started")
    time.sleep(20)


@shared_task
def send_email_func():
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Test'
        message = "Hello world!"
        to_email = user.email
        send_mail(
            mail_subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=True,
        )
        print(to_email)
        print("Email sent")
