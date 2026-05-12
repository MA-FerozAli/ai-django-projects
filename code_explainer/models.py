from django.db import models

# Create your models here.
class Code_History(models.Model):
    code_snippet=models.TextField()
    code_explanation=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Explaination for {self.created_at}   "