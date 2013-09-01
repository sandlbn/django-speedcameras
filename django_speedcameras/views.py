from django.views.generic import ListView
from django.conf import settings
from models import SpeedCamera


class GoogleSpeedCamera(ListView):

    template_name = 'django_speedcameras/google_maps.html'
    context_object_name = 'cameras'
    queryset = SpeedCamera

    def get_queryset(self):

        queryset = self.queryset.objects.filter(active=True)

        return queryset
