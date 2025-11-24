from rest_framework import serializers
from .models import Place, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'title',
            'image',
            'caption',
            'taken_at',
            'uploaded_at',
        ]


class PlaceSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'latitude',
            'longitude',
            'created_at',
            'url',
            'photos',
        ]

    def get_url(self, obj):
        return obj.get_absolute_url()
