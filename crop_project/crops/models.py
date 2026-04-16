from django.db import models

class CropData(models.Model):
    year = models.IntegerField()
    region = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    production = models.FloatField(null=True, blank=True)
    yield_amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.crop} ({self.region}, {self.year})"