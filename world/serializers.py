from rest_framework import serializers
from .models import Aircraft, Mission, Weapon, WorldBorder
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class WorldBorderSerializer(GeoFeatureModelSerializer):
    """A class to serialize locations as GeoJSON compatible data"""

    class Meta:
        model = WorldBorder
        geo_field = "geom"

        # you can also explicitly declare which fields you want to include
        # # as with a ModelSerializer.
        fields = ("name", "abbrevname", "fips_code", "wb_cntry")


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = (
            "weapon_name",
            "weapon_type",
            "weapon_class",
            "nbr_bombs",
            "weapon_description",
            "country",
            "alt_weapon_name",
        )


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ("aircraft", "name", "full_name", "type", "hyperlink")


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
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
        )
