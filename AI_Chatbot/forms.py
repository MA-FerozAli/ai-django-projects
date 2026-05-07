from django import forms

class ChatForm(forms.Form):
    user_message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type your message...','rows':3}),label="")