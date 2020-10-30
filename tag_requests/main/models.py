from django.db import models

class Url_table(models.Model):
    url = models.URLField()
    date = models.TimeField()
    text = models.TextField()
