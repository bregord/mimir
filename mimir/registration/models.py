from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
       user        = models.OneToOneField(User)
       picture     = models.ImageField(upload_to='profile_images', blank=True,)
       description = models.CharField(max_length=500,blank=True)
       interests   = models.CharField(max_length=200,blank=True)
       website     = models.URLField(max_length=200,blank=True)
       
       def __unicode__(self):
               return self.user.username
      # picture = models.ImageField(upload_to='profile_images', blank=True,)
