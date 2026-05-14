from django import forms
from django.core.exceptions import ValidationError
class PDFUploadForm(forms.Form):
    pdf_file=forms.FileField(required=True,label=Upload PDF)
    summary_length=forms.ChoiceField(choices=[
        ('short','Short (2-3 sentences)'),
        ('medium','Medium (1-2 parahgraph)'),
        ('detailed','Detailed (full breakdown)')
    ])
    def clean_pdf_file(self):
        file=self.cleaned_data.get['pdf_file']
        if file :
            if not file.name.endswith('.pdf'):
                raise ValidationError("File must in  .pdf format only")
            max_size=5 *1024 * 1024
            if file.size > max_size :
                raise ValidationError("File must be upto 5MB only")
        return file
            
