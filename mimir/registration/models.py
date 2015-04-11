from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seminar(models.Model):
       author   = models.ForeignKey(User)
       topic    = models.CharField(max_length=300)
       title    = models.CharField(max_length=50)
       contents = models.TextField()

class Discussions(models.Model):
       author   = models.ForeignKey(User)
       seminar  = models.ForeignKey('Seminar',related_name='seminar')
       contents = models.TextField()
       line     = models.IntegerField()
       parent   = models.ForeignKey('self',related_name='discussion_parent',blank=True) # for replies to discussions


