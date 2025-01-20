# webinars/forms.py
from django import forms
from .models import *

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

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'author',
            'content',
        ]

class BlogVerificationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'content',
            'author',
            'is_verified'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = [
            'user',
            'content',
        ]
