from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=140)
    content = models.TextField()
