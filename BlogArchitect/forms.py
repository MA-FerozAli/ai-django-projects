from django import forms

class BlogForm(forms.Form):
    Topic=forms.CharField(widget=forms.Textarea(),label="")