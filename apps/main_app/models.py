from django.db import models

class Rescuee(models.Model):
    name = models.CharField(max_length=200)
    disaster = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    children = models.CharField(max_length=200)
    senior = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
