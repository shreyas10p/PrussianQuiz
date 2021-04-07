from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .storage import PrivateMediaStorage
from .utils import generate_image_id
from datetime import datetime 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.BigIntegerField(null=True,blank=True)
    employer = models.CharField(max_length=200,blank=True)
    job_title = models.CharField(max_length=200,blank=True)
    profile_picture = models.ImageField(storage = PrivateMediaStorage(),blank=True)

    def get_age(self):
        if(self.birth_date):
            bday = datetime.strptime(str(self.birth_date), '%Y-%m-%d')
            today = datetime.today()
            return str(today.year - bday.year) 
        return 
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

