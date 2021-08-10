from django.db import connection, transaction
from django.contrib.gis.db import models


class Mission(models.Model):
    wwi_id = models.IntegerField("WWI_ID")
    msndate = models.CharField("MSNDATE", max_length=255)
    operation = models.CharField("OPERATION", max_length=255)
    country = models.CharField("COUNTRY", max_length=255)
    service = models.CharField("SERVICE", max_length=255)
    unit = models.CharField("UNIT", max_length=255)
    mds = models.CharField("MDS", max_length=255)
    missionnum = models.FloatField("MISSIONNUM")
    departure = models.CharField("DEPARTURE", max_length=255)
    takeofftime = models.CharField("TAKEOFFTIME", max_length=255)
    numberofplanesattacking = models.FloatField("NUMBEROFPLANESATTACKING")
    callsign = models.CharField("CALLSIGN", max_length=255)
    weaponsexpended = models.FloatField("WEAPONSEXPENDED")
    weapontype = models.CharField("WEAPONTYPE", max_length=255)
    weaponweight = models.FloatField("WEAPONWEIGHT")
    bombload = models.FloatField("BOMBLOAD")
    latitude = models.FloatField("LATITUDE")
    longitude = models.FloatField("LONGITUDE")
    tgtlocation = models.CharField("TGTLOCATION", max_length=255)
    tgtcountry = models.CharField("TGTCOUNTRY", max_length=255)
    tgttype = models.CharField("TGTTYPE", max_length=255)
    takeoffbase = models.CharField("TAKEOFFBASE", max_length=255)
    takeofflatitude = models.FloatField("TAKEOFFLATITUDE")
    takeofflongitude = models.FloatField("TAKEOFFLONGITUDE")
    bda = models.CharField("BDA", max_length=255)
    enemyaction = models.CharField("ENEMYACTION", max_length=1024)
    routedetails = models.CharField("ROUTEDETAILS", max_length=255)
    isrcollected = models.CharField("ISRCOLLECTED", max_length=255)
    friendlycasualties = models.FloatField("FRIENDLYCASUALTIES")
    friendlycasualties_verbose = models.CharField(
        "FRIENDLYCASUALTIES_VERBOSE", max_length=255
    )
    weather = models.CharField("WEATHER", max_length=255)
    altitude = models.FloatField("ALTITUDE")


class WorldBorder(models.Model):
    year = models.CharField("year", max_length=4)
    area = models.FloatField()
    name = models.CharField(max_length=40, default="", null=True)
    abbrevname = models.CharField(max_length=12, default="", null=True)
    fips_code = models.CharField(max_length=2, default="", null=True)
    wb_cntry = models.CharField(max_length=3, default="", null=True)
    geom = models.MultiPolygonField(srid=4326)


class Border1880(models.Model):
    year = models.CharField("year", max_length=4, default=1880)
    area = models.FloatField()
    name = models.CharField(max_length=40, default="", null=True)
    abbrevname = models.CharField(max_length=12, default="", null=True)
    fips_code = models.CharField(max_length=2, default="", null=True)
    wb_cntry = models.CharField(max_length=3, default="", null=True)
    geom = models.MultiPolygonField(srid=4326)


class Border1914(models.Model):
    year = models.CharField("year", max_length=4, default=1914)
    area = models.FloatField()
    name = models.CharField(max_length=40, default="", null=True)
    abbrevname = models.CharField(max_length=12, default="", null=True)
    fips_code = models.CharField(max_length=2, default="", null=True)
    wb_cntry = models.CharField(max_length=3, default="", null=True)
    geom = models.MultiPolygonField(srid=4326)


class Border1920(models.Model):
    year = models.CharField("year", max_length=4, default=1920)
    area = models.FloatField()
    name = models.CharField(max_length=40, default="", null=True)
    abbrevname = models.CharField(max_length=12, default="", null=True)
    fips_code = models.CharField(max_length=2, default="", null=True)
    wb_cntry = models.CharField(max_length=3, default="", null=True)
    geom = models.MultiPolygonField(srid=4326)


class Aircraft(models.Model):
    id = models.IntegerField(primary_key=True)
    aircraft = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    hyperlink = models.CharField(max_length=255)


class Weapon(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255)
    weapon_name = models.CharField(max_length=255)
    weapon_type = models.CharField(max_length=255)
    weapon_class = models.CharField(max_length=255)
    nbr_bombs = models.IntegerField()
    alt_weapon_name = models.CharField(max_length=255)
    weapon_description = models.CharField(max_length=255)
