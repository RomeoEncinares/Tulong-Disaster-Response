from django.db import models

class Rescuee(models.Model):
    name = models.CharField(max_length=100)
    disaster = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    total = models.IntegerField()
    children = models.IntegerField()
    senior = models.IntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
