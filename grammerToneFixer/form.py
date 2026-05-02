from django import forms
TONE=[
    ('','select Tone'),
    ('professional',"Professional"),
    ('casual','Casual'),
    ('funny','Funny'),
]
class GrammerForm(forms.Form):
    UserText=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':50}))
    tone=forms.ChoiceField(choices=TONE)

