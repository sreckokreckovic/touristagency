from rest_framework.viewsets import ModelViewSet
from offers.models import Offer, Category
from .serializers import OfferSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.all()
