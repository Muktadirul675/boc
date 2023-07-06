from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . import models
from django.core.mail import send_mail
from boc import settings

@receiver(post_save,sender=User)
def create_profile(sender,instance,**kwargs):
    if models.Profile.objects.filter(user=instance).exists():
        # print("not created")
        pass
    else:
        models.Profile.objects.create(user=instance)
        send_mail(
            'Registration Successful', 'Welcome to BOC!', settings.EMAIL_HOST_USER, [instance.email], fail_silently=True,
        )
        # print(f"Profile created for {new_profile.user}")
