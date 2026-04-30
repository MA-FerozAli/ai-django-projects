from django import forms

class SummarizeForm(forms.Form):
    text= forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control', # This is the Bootstrap magic class
            'placeholder': 'Paste your text here...',
            'rows': 8
        }),
        label="")