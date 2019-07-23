from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    opening_time = models.TimeField('opening time')
    closing_time = models.TimeField('closing time')

    def __str__(self):
        return self.name
# Create your models here.
