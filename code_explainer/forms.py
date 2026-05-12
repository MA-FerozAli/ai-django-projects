from django  import forms
from .models import Code_History

class CodeForm(forms.Form):
    user_code=forms.CharField(widget=forms.Textarea(),label="Paste your code Here")