from django.db import models

import registration.models

class editorPage(models.Model):# Create your models here.
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()


