# webinars/forms.py
from django import forms
from .models import Webinar, Registration

class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['title', 'description', 'image', 'date', 'link', 'price']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['webinar']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
