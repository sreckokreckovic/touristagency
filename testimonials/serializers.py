from django.contrib.auth.models import User
from rest_framework import serializers

from testimonials.models import Testimonial


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


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id',
            'first_name',
            'last_name',
            'description',

        ]
        read_only_fields = ['id']
