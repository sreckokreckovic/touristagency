from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer



class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
         return Reservation.objects.all()
        return Reservation.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

