from django.db import models

# Create your models here.
class PageViews(models.Model):
    pageViewCount = models.IntegerField(default = 0)
    