from django.contrib.gis.db import models

from swachhbharat.utils import TimeStampMixin


class Image(TimeStampMixin):
    file = models.ImageField(upload_to='images/%Y/%m/%d')
    location = models.PointField(null=True)
