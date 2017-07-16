# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from webcams.models import Resort, Image
from webcams.serializers import ResortSerializer, ImageSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
def index(request, path=''):
    return render(request, 'index.html')
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('resort-list', request=request, format=format),
        'snippets': reverse('image-list', request=request, format=format)
    })

class ResortViewSet(viewsets.ModelViewSet):
    queryset = Resort.objects.all()
    serializer_class = ResortSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
