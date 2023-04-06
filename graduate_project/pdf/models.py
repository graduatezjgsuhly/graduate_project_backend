from django.db import models

class PDF(models.Model):
    name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
# Create your models here.
