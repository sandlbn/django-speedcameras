from django.db import models

class SpeedCamera(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name


class PolygonPoint(models.Model):

    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    speed_camera = models.ForeignKey(SpeedCamera)

    def __unicode__(self):
        return u'Lat {0}, Lng {1}'.format(self.lat, self.lng)
