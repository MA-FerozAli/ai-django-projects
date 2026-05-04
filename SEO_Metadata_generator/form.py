from django import forms

class SEOForm(forms.Form):
    blog_title=forms.CharField(max_length=100)
    keywords=forms.CharField(max_length=255)