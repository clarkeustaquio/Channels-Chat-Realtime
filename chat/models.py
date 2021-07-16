from django.db import models

# Create your models here.
class Chat(models.Model):
    chat = models.CharField(max_length=150)

    def __str__(self):
        return self.chat