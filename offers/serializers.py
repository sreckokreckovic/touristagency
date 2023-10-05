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
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())


    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
            'description',
            'price',
            'number_of_people',
            'duration',
            'start_date',
            'end_date',
            'category',
            'media',
        ]

        read_only_fields = ['id']

    def get_media(self, obj):
        media_objects = Media.objects.filter(offer=obj)

        media_serializer = MediaSerializer(media_objects, many=True, context=self.context)
        return media_serializer.data
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation

class OfferTitleIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
        ]