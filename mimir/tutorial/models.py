from django.db import models
from django_markdown.models import MarkdownField



class editorPage(models.Model):# Create your models here.
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body =  MarkdownField()

