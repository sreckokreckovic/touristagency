from django.contrib.auth.models import User
from rest_framework import serializers

from offers.models import Offer, Category
from reservations.models import Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',

        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class OfferSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
            'description',
            'price',
            'category',

        ]


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    offer = serializers.PrimaryKeyRelatedField(queryset=Offer.objects.all())

    class Meta:
        model = Reservation
        fields = [
            'id',
            'user',
            'offer',
            'user',
            'created_at',
            'updated_at',

        ]

        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['offer'] = OfferSerializer(instance.offer).data
        return representation
