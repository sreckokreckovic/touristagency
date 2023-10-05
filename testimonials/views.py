from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from testimonials.models import Testimonial
from testimonials.serializers import TestimonialSerializer


class TestimonialViewSet(ModelViewSet):
    serializer_class = TestimonialSerializer
    permission_classes = []

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    def get_queryset(self):
        return Testimonial.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You need to be authenticated")

        serializer.save(user=self.request.user)
