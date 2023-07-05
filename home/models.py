from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to="profiles/",default="user_bvpgnf.png")
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    boc_id = models.CharField(max_length=6,blank=True)

    def __str__(self):
        return f'{self.user}'
