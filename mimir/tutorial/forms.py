from django import forms
from django_markdown.widgets import MarkdownWidget
from tutorial.models import editorPage

class editorPageForm(forms.Form):
    #title = forms.CharField(max_length=128, help_text="Title")
    data = forms.CharField(widget = MarkdownWidget())
    class Meta:
        model = editorPage
        fields = ('data', 'content')
