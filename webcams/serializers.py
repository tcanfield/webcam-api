from rest_framework import serializers
from webcams.models import Resort, Image

class ResortSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='image-detail')
    class Meta:
        model = Resort
        fields = ('url', 'id', 'name', 'resort_url', 'images')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('url', 'id', 'name', 'image_url', 'resort')
