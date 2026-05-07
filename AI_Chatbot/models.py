from django.db import models

# Create your models here.
class ConversationModel(models.Model):
    session_id=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

class MessageModel(models.Model):
    converstion=models.ForeignKey(ConversationModel,on_delete=models.CASCADE)
    role=models.CharField(max_length=255)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} : {self.message[:30]}"