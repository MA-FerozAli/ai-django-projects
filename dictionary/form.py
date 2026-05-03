from django import forms

class DictionaryForm(forms.Form):
    word = forms.CharField(
        label="Word",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter any word...",
            "class": "word-input",
            "autocomplete": "off",
        }),
    )