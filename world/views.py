from rest_framework.generics import ListAPIView
from .models import WorldBorder, Mission, Weapon, Aircraft
from .serializers import (
    AircraftSerializer,
    MissionSerializer,
    WeaponSerializer,
    WorldBorderSerializer,
)
from django_filters import rest_framework as filters


class WorldBorderList(ListAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["year", "area", "name", "abbrevname", "fips_code", "wb_cntry"]

class MissionList(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = [
        "wwi_id",
        "msndate",
        "operation",
        "country",
        "service",
        "unit",
        "mds",
        "missionnum",
        "departure",
        "takeofftime",
        "numberofplanesattacking",
        "callsign",
        "weaponsexpended",
        "weapontype",
        "weaponweight",
        "bombload",
        "latitude",
        "longitude",
        "tgtlocation",
        "tgtcountry",
        "tgttype",
        "takeoffbase",
        "takeofflatitude",
        "takeofflongitude",
        "bda",
        "enemyaction",
        "routedetails",
        "isrcollected",
        "friendlycasualties",
        "friendlycasualties_verbose",
        "weather",
        "altitude",
    ]


class AircraftList(ListAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["id", "aircraft", "name", "full_name", "type", "hyperlink"]


class WeaponList(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = [
        "id",
        "weapon_name",
        "weapon_type",
        "weapon_class",
        "nbr_bombs",
        "weapon_description",
        "country",
        "alt_weapon_name",
    ]
