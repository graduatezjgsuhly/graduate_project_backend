from django.db import models
from datetime import datetime
class PDF(models.Model):
    name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
# Create your models here.

class Car(models.Model):
    def get_suffix(self, filename=None):
        filename = filename or self.filename
        if filename and '.' in filename:
            return filename.rsplit(".", 1)[1]
	
    def generate_filename(self, filename):
        suffix = self.get_suffix(filename)
        time_str = datetime.now().strftime('%y%m%d%H%M%S')
        unique_filename = '{}{}'.format(time_str, 1)
        if suffix:
            unique_filename = '{}.{}'.format(unique_filename, suffix)
        url = "files/{}".format(unique_filename)
        return url
    photo = models.FileField(upload_to=generate_filename)
    filename = models.CharField(verbose_name="文件名称", max_length=128, blank=True, null=True)