from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(use_url=True)
    location = GeometryField(required=False)

    class Meta:
        model = Image
        fields = ('id', 'file', 'location', )
