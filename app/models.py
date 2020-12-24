from django.db import models


# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    port = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.name
