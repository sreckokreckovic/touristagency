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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Testimonial
        fields = [
            'id',
            'title',
            'description',
            'user',
        ]
        read_only_fields = ['id', 'user']
