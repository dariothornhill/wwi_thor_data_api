from rest_framework.generics import (ListAPIView)
from .models import WorldBorder, Mission, Weapon, Aircraft
from .serializers import  AircraftSerializer, MissionSerializer, WeaponSerializer, WorldBorderSerializer
import django_filters.rest_framework
class WorldBorderList(ListAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class= WorldBorderSerializer
    
class MissionList(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class= MissionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class AircraftList(ListAPIView):
    queryset = Aircraft.objects.all()
    serializer_class= AircraftSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
class WeaponList(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class= WeaponSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]