from django import forms
from .models import Facts

class CompanyFactForm(forms.ModelForm):
    class Meta:
        model=Facts
        fields=['title','content']
class QuestionForm(forms.Form):
    question=forms.CharField(widget=forms.Textarea,
    label="Ask Questiion")
