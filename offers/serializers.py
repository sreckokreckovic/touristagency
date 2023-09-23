from rest_framework import serializers
from offers.models import Offer, Category, Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'id',
            'path',
            'offer',
        ]



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]
        read_only_fields = ['id']


class OfferSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
            'description',
            'price',
            'category',
            'media',
        ]

        read_only_fields = ['id']

    def get_media(self, obj):
        media_objects = Media.objects.filter(offer=obj)

        media_serializer = MediaSerializer(media_objects, many=True, context=self.context)
        return media_serializer.data