from email import message
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    content=models.TextField(max_length=500)

    def __str__(self):
            return 'Message from '+self.name