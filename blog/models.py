from django.db import models

# Create your models here.

class blog(models.Model):
  blog_title = models.CharField(max_length=255)
  blog_desc = models.CharField(max_length=255)
