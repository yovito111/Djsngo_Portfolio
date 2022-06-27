from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
import datetime
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
