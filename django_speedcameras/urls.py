# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django_speedcameras.views import GoogleSpeedCamera
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'django_theatre.views',
    url(r'^$', GoogleSpeedCamera.as_view(), name='google_map'),
)
