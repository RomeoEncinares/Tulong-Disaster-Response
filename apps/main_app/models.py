from django.db import models

class Rescuee(models.Model):
    name = models.CharField(blank=True, max_length=100)
    disaster = models.CharField(blank=True, max_length=200)
    location = models.CharField(blank=True, max_length=200)
    total = models.IntegerField(blank=True, )
    children = models.IntegerField(blank=True, )
    senior = models.IntegerField(blank=True, )
    message = models.CharField(blank=True, max_length=200)
    status_choices = (
    ('Waiting','Waiting for Rescuers'),
    ('Going','Rescuers on the Way'),
    )
    status = models.CharField(max_length=30, choices=status_choices, blank=True, default=status_choices[0][0])

    def __str__(self):
        return self.name

# Create your models here.
