from django.db.models import Count
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from offers.models import Offer, Category, Media
from .serializers import OfferSerializer, CategorySerializer
from rest_framework import permissions, status, generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class IsReadOnlyOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_staff


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = []

    def get_queryset(self):
        return Category.objects.all()


class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer
    permission_classes = [IsReadOnlyOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','title']


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


class TopOffersView(generics.ListAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self):
        top_offers = Offer.objects.annotate(num_reservations=Count('reservation')).order_by('-num_reservations')[:3]
        return top_offers


class OfferListByCategory(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
            offers = Offer.objects.filter(category=category)
            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
