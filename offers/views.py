from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from offers.models import Offer, Category
from .serializers import OfferSerializer, CategorySerializer
from rest_framework import permissions


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
