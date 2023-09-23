from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from offers.models import Offer, Category, Media
from .serializers import OfferSerializer, CategorySerializer
from rest_framework import permissions, status


class IsReadOnlyOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_staff


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Category.objects.all()


class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer
    permission_classes = [IsReadOnlyOrAdmin]

    def get_queryset(self):
        return Offer.objects.all()

    def create(self, request, *args, **kwargs):
        offer_serializer = self.get_serializer(data=request.data)
        offer_serializer.is_valid(raise_exception=True)
        offer = offer_serializer.save()

        images = request.FILES.getlist('media')
        for image in images:
            media = Media.objects.create(offer=offer, path=image)

        return Response(status=status.HTTP_201_CREATED)
