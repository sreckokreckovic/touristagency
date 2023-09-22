from rest_framework import serializers

from testimonials.models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id',
            'title',
            'description',
            'user',
        ]
        read_only_fields = ['id','user']