from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, default="New item")
    checked = models.BooleanField(default=False)
