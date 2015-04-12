from django import forms

class UserForm(forms.Form):
        username     = forms.CharField(label='Username')
        password     = forms.CharField(label='Password',widget=forms.PasswordInput())
        email        = forms.CharField(label='Email',widget=forms.EmailInput())
        description  = forms.CharField(label='Describe yourself',widget=forms.Textarea)
        interests    = forms.CharField(label='What are your interests?', help_text="semi-colon separated")
        website      = forms.URLField(label='Your website URL')
        picture      = forms.FileField(label='Profile Picture')
