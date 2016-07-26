from rest_framework import viewsets

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-created_on')
    serializer_class = ImageSerializer
