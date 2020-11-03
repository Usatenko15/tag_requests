from django.db import models


class Url_table(models.Model):
    url = models.URLField()
    tags_list = models.CharField(max_length=2555)
    time = models.DateTimeField()
