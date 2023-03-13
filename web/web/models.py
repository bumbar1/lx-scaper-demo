from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=128)
    image_url = models.URLField()

