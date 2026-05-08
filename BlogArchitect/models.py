from django.db import models

# Create your models here.
class Blog(models.Model):
    topic=models.CharField(max_length=200)
    outline=models.CharField(max_length=255)
    full_blog=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    