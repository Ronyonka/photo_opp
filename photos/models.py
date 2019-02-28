from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name