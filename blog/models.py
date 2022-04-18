from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    slg = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(default='', upload_to='blogs', null=True)
    active = models.BooleanField(default=False)
    created_At = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
