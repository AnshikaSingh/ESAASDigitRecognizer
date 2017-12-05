from rest_framework import serializers
from imageupload.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail', 'title', 'description', )
        read_only_fields = ('thumbnail',)

