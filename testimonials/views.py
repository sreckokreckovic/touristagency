from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from testimonials.models import Testimonial
from testimonials.serializers import TestimonialSerializer


class TestimonialViewSet(ModelViewSet):
    serializer_class = TestimonialSerializer
    permission_classes = []

    def get_queryset(self):
        return Testimonial.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You need to be authenticated")

        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only administrator can delete")

        instance.delete()
