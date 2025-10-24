from django.db import models
from datetime import date # Import the date class
from django.utils import timezone

class Farmer(models.Model):
    employee = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    today_date = models.DateField(default=timezone.now) 
    crop = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    seed = models.BooleanField(default=False)
    pesticide = models.BooleanField(default=False)
    fertilizer = models.BooleanField(default=False)
    drip = models.BooleanField(default=False)
    machinery = models.BooleanField(default=False)
    nursery = models.BooleanField(default=False)
    sprayer = models.BooleanField(default=False)
    location = models.TextField()

    # New optional fields
    next_visit = models.DateField(blank=True, null=True)
    others = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
