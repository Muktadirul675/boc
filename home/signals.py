from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . import models

@receiver(post_save,sender=User)
def create_profile(sender,instance,**kwargs):
    if models.Profile.objects.filter(user=instance).exists():
        # print("not created")
        pass
    else:
        models.Profile.objects.create(user=instance)
        # print(f"Profile created for {new_profile.user}")
