from django.db import models


class Gallery(models.Model):
    url = models.URLField
    name = models.CharField(max_length=150)


