from django.db import models

# Create your models here.


class Article(models.Model):
    title: str = models.CharField(max_length=100)
    content: str = models.TextField()
    active: bool = models.BooleanField(default=False)
