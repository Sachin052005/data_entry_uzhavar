from django.db import models
from datetime import date # Import the date class

class Farmer(models.Model):
    employee = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
    # New field added. It is required, so we set a default for existing records.
    # The default is set to a specific date to satisfy makemigrations.
    today_date = models.DateField(default=date(2024, 1, 1), auto_now_add=False)
    
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
