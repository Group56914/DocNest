from django.db import models

# Create your models here.
class Upload(models.Model):
    file=models.FileField()
    
    def __str__(self):
        return str(self.file)
