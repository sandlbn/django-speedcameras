from django.contrib.gis.db import models

class SpeedCamera(models.Model):
    name = models.CharField(max_length=255)
    poly = models.PolygonField(srid=4326)
    description = models.CharField(max_length=255)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name
