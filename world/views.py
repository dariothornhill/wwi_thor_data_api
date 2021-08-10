from rest_framework.generics import (ListAPIView)
from .models import WorldBorder, Mission, Weapon, Aircraft
from .serializers import  AircraftSerializer, MissionSerializer, WeaponSerializer, WorldBorderSerializer

class WorldBorderList(ListAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class= WorldBorderSerializer
    
class MissionList(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class= MissionSerializer

class AircraftList(ListAPIView):
    queryset = Aircraft.objects.all()
    serializer_class= AircraftSerializer
class WeaponList(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class= WeaponSerializer