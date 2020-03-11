from django.db import models

# Create your models here.
class TextFile(models.Model):
    content = models.FileField(upload_to = 'documents/')
