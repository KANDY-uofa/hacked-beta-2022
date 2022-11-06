from django.db import models
import geocoder

# Create your models here.
class Data(models.Model):
    location = models.CharField(max_length = 100, null = True)
    reports_2021 = models.PositiveBigIntegerField()
    reports_2022 = models.PositiveBigIntegerField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Data'
        
    def save(self,*args,**kwargs):
        self.latitude = geocoder.osm(self.location).lat
        self.longitude = geocoder.osm(self.location).lng
        return super().save(*args, **kwargs)

    def update(self,*args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.location
