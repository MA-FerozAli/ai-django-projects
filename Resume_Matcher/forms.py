from  django import forms

class ResumeForm(forms.Form):
    resume_text=forms.CharField(widget=forms.Textarea,label="Paste Your Resume")
    job_description=forms.CharField(widget=forms.Textarea,label="Paste Your Job Description")