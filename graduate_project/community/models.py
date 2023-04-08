from django.db import models
from django.utils import timezone
# Create your models here.
class comment(models.Model): ##评论
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
    comment_text =models.TextField()
    pdf_file = models.FileField(upload_to=generate_filename)
    user_name = models.CharField(max_length=100)
    created_time = models.DateTimeField(default=timezone.now)
    comment_id = models.IntegerField(null=True)
class comment_post(models.Model):##评论区
    comment_post_text = models.TextField()
    user_post_name = models.CharField(max_length=100)
    created_time = models.DateTimeField(default=timezone.now)
    comment_id = models.IntegerField(null=True)