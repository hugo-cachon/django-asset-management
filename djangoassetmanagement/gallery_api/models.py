from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey('auth.User', related_name='galleries', on_delete=models.CASCADE, default=1)


