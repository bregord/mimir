from django import forms
from django_markdown.widgets import MarkdownWidget
from tutorial.models import editorPage

class editorPageForm(forms.Form):
    body = forms.CharField(widget = MarkdownWidget(), help_text='Lesson Goes Here')
    title = forms.CharField(max_length=128, help_text="Title")
    class Meta:
        model = editorPage
        fields = ('body,title,')
