from django.contrib.gis.maps.google.gmap import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GPolygon
from django.views.generic import TemplateView
from django.conf import settings
from models import SpeedCamera

class GoogleSpeedCamera(TemplateView):

    template_name = 'django_speedcameras/google_maps.html'

    def get_context_data(self, **kwargs):

        context = super(GoogleSpeedCamera,self).get_context_data(**kwargs)

        queryset = SpeedCamera.objects.filter(active=True)
        gpolygons = []

        for camera in queryset:
            gpolygon = GPolygon(camera.poly)
            gpolygons.append(gpolygon)

        google_maps = GoogleMap(
            center = (0,0),
            zoom = 5,
            key=settings.GOOGLE_MAPS_API_PASSWORD,
            polygons = gpolygons
        )
        context["google"] = google_maps

        return context
