from django import forms
from django_markdown.widgets import MarkdownWidget
from tutorial.models import editorPage

import tutorial.models


class editorPageForm(forms.Form):
    title = forms.CharField(max_length=128)
    #content = forms.CharField(widget = forms.Textarea)
    data = forms.CharField(widget = MarkdownWidget())
    class Meta:
        model = editorPage
        fields = ('data')

#class MyCustomForm(forms.Form):
 #   content = forms.CharField(widget=MarkdownWidget())
  #  content2 = MarkdownFormField()
