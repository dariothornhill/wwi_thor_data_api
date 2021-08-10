import os

from django.contrib.gis.utils import layermapping
from .models import (
    Aircraft,
    Mission,
    Weapon,
    WorldBorder,
    Border1880,
    Border1914,
    Border1920,
)
from django.db import connection
import pandas as pd

country_shape_files = [
    {
        "path": os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data/1880/cntry1880.shp")
        ),
        "class": Border1880,
    },
    {
        "path": os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data/1914/cntry1914.shp")
        ),
        "class": Border1914,
    },
    {
        "path": os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data/1920/cntry1920.shp")
        ),
        "class": Border1920,
    },
]

# Auto-generated `LayerMapping` dictionary for cntry1920 model
world_mapping = {
    "area": "AREA",
    "name": "NAME",
    "abbrevname": "ABBREVNAME",
    "fips_code": "FIPS_CODE",
    "wb_cntry": "WB_CNTRY",
    "geom": "MULTIPOLYGON",
}


def run(verbose=True):
    for item in country_shape_files:
        ln = layermapping.LayerMapping(
            item.get("class"),
            item.get("path"),
            world_mapping,
            transform=True,
            encoding="iso-8859-1",
        )
        try:
            ln.save(strict=False, verbose=verbose)
            cls = item.get("class")
            update_world(cls)

        except Exception as e:
            print(e)


def update_world(cls):
    sql = f"INSERT INTO {WorldBorder._meta.db_table} (year, area, name, abbrevname, fips_code, wb_cntry, geom) SELECT year, area, name, abbrevname, fips_code, wb_cntry, geom FROM {cls._meta.db_table};"
    with connection.cursor() as cursor:
        cursor.execute(sql)


def import_missions():
    mission_csv = pd.read_csv(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data/ww1_missions.csv")
        )
    )
    "WWI_ID", "MSNDATE", "OPERATION", "COUNTRY", "SERVICE", "UNIT", "MDS", "MISSIONNUM", "DEPARTURE", "TAKEOFFTIME", "NUMBEROFPLANESATTACKING", "CALLSIGN", "WEAPONSEXPENDED", "WEAPONTYPE", "WEAPONWEIGHT", "BOMBLOAD", "LATITUDE", "LONGITUDE", "TGTLOCATION", "TGTCOUNTRY", "TGTTYPE", "TAKEOFFBASE", "TAKEOFFLATITUDE", "TAKEOFFLONGITUDE", "BDA", "ENEMYACTION", "ROUTEDETAILS", "ISRCOLLECTED", "FRIENDLYCASUALTIES", "FRIENDLYCASUALTIES_VERBOSE", "WEATHER", "ALTITUDE"
    mission_csv["INDEX"] = mission_csv["WWI_ID"]
    mission_csv.set_index("INDEX", inplace=True)

    mission_csv["WEAPONSEXPENDED"].fillna(-1, inplace=True)
    mission_csv["WEAPONWEIGHT"].fillna(-1, inplace=True)
    mission_csv["BOMBLOAD"].fillna(-1, inplace=True)
    mission_csv["LATITUDE"].fillna(0, inplace=True)
    mission_csv["LONGITUDE"].fillna(0, inplace=True)
    mission_csv["TAKEOFFLATITUDE"].fillna(0, inplace=True)
    mission_csv["TAKEOFFLONGITUDE"].fillna(0, inplace=True)
    mission_csv["FRIENDLYCASUALTIES"].fillna(-1, inplace=True)
    mission_csv["ALTITUDE"].fillna(-1, inplace=True)
    mission_csv["NUMBEROFPLANESATTACKING"].fillna(-1, inplace=True)
    mission_csv["MSNDATE"].fillna('Unknown', inplace=True)
    mission_csv["OPERATION"].fillna('Unknown', inplace=True)
    mission_csv["COUNTRY"].fillna('Unknown', inplace=True)
    mission_csv["SERVICE"].fillna('Unknown', inplace=True)
    mission_csv["UNIT"].fillna('Unknown', inplace=True)
    mission_csv["MDS"].fillna('Unknown', inplace=True)
    mission_csv["MISSIONNUM"].fillna(-1, inplace=True)
    mission_csv["DEPARTURE"].fillna('Unknown', inplace=True)
    mission_csv["TAKEOFFTIME"].fillna('Unknown', inplace=True)
    mission_csv["CALLSIGN"].fillna('Unknown', inplace=True)
    mission_csv["WEAPONTYPE"].fillna('Unknown', inplace=True)
    mission_csv["TGTLOCATION"].fillna('Unknown', inplace=True)
    mission_csv["TGTCOUNTRY"].fillna('Unknown', inplace=True)
    mission_csv["TGTTYPE"].fillna('Unknown', inplace=True)
    mission_csv["TAKEOFFBASE"].fillna('Unknown', inplace=True)
    mission_csv["BDA"].fillna('Unknown', inplace=True)
    mission_csv["ENEMYACTION"].fillna('Unknown', inplace=True)
    mission_csv["ROUTEDETAILS"].fillna('Unknown', inplace=True)
    mission_csv["ISRCOLLECTED"].fillna('Unknown', inplace=True)
    mission_csv["FRIENDLYCASUALTIES_VERBOSE"].fillna('Unknown', inplace=True)
    mission_csv["WEATHER"].fillna('Unknown', inplace=True)

    missions = [
        Mission(
            wwi_id=mission_csv.loc[row]["WWI_ID"],
            msndate=mission_csv.loc[row]["MSNDATE"],
            operation=mission_csv.loc[row]["OPERATION"],
            country=mission_csv.loc[row]["COUNTRY"],
            service=mission_csv.loc[row]["SERVICE"],
            unit=mission_csv.loc[row]["UNIT"],
            mds=mission_csv.loc[row]["MDS"],
            missionnum=mission_csv.loc[row]["MISSIONNUM"],
            departure=mission_csv.loc[row]["DEPARTURE"],
            takeofftime=mission_csv.loc[row]["TAKEOFFTIME"],
            numberofplanesattacking=mission_csv.loc[row]["NUMBEROFPLANESATTACKING"],
            callsign=mission_csv.loc[row]["CALLSIGN"],
            weaponsexpended=mission_csv.loc[row]["WEAPONSEXPENDED"],
            weapontype=mission_csv.loc[row]["WEAPONTYPE"],
            weaponweight=mission_csv.loc[row]["WEAPONWEIGHT"],
            bombload=mission_csv.loc[row]["BOMBLOAD"],
            latitude=mission_csv.loc[row]["LATITUDE"],
            longitude=mission_csv.loc[row]["LONGITUDE"],
            tgtlocation=mission_csv.loc[row]["TGTLOCATION"],
            tgtcountry=mission_csv.loc[row]["TGTCOUNTRY"],
            tgttype=mission_csv.loc[row]["TGTTYPE"],
            takeoffbase=mission_csv.loc[row]["TAKEOFFBASE"],
            takeofflatitude=mission_csv.loc[row]["TAKEOFFLATITUDE"],
            takeofflongitude=mission_csv.loc[row]["TAKEOFFLONGITUDE"],
            bda=mission_csv.loc[row]["BDA"],
            enemyaction=mission_csv.loc[row]["ENEMYACTION"],
            routedetails=mission_csv.loc[row]["ROUTEDETAILS"],
            isrcollected=mission_csv.loc[row]["ISRCOLLECTED"],
            friendlycasualties=mission_csv.loc[row]["FRIENDLYCASUALTIES"],
            friendlycasualties_verbose=mission_csv.loc[row][
                "FRIENDLYCASUALTIES_VERBOSE"
            ],
            weather=mission_csv.loc[row]["WEATHER"],
            altitude=mission_csv.loc[row]["ALTITUDE"],
        )
        for row in mission_csv["WWI_ID"]
    ]
    Mission.objects.bulk_create(missions)


def import_aircraft():
    aircraft_csv = pd.read_csv(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data/ww1_aircraft.csv")
        )
    )
    "ID", "AIRCRAFT", "NAME", "FULL_NAME", "TYPE", "HYPERLINK"
    aircraft_csv["WWI_ID"] = aircraft_csv["ID"]
    aircraft_csv.set_index("WWI_ID", inplace=True)
    aircraft = [
        Aircraft(
            id=aircraft_csv.loc[row]["ID"],
            aircraft=aircraft_csv.loc[row]["AIRCRAFT"],
            name=aircraft_csv.loc[row]["NAME"],
            full_name=aircraft_csv.loc[row]["FULL_NAME"],
            type=aircraft_csv.loc[row]["TYPE"],
            hyperlink=aircraft_csv.loc[row]["HYPERLINK"],
        )
        for row in aircraft_csv["ID"]
    ]
    Aircraft.objects.bulk_create(aircraft)


def import_weapons():
    weapon_csv = pd.read_csv(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "data/ww1_weapon.csv"))
    )
    "ID", "COUNTRY", "WEAPON_NAME", "WEAPON_TYPE", "WEAPON_CLASS", "NBR_BOMBLETS", "ALT_WEAPON_NAME", "WEAPON_DESCRIPTION"
    weapon_csv["WWI_ID"] = weapon_csv["ID"]
    weapon_csv.set_index("WWI_ID", inplace=True)
    weapon_csv["NBR_BOMBLETS"].fillna(0, inplace=True)
    weapons = [
        Weapon(
            id=weapon_csv.loc[row]["ID"],
            country=weapon_csv.loc[row]["COUNTRY"],
            weapon_name=weapon_csv.loc[row]["WEAPON_NAME"],
            weapon_type=weapon_csv.loc[row]["WEAPON_TYPE"],
            weapon_class=weapon_csv.loc[row]["WEAPON_CLASS"],
            nbr_bombs=weapon_csv.loc[row]["NBR_BOMBLETS"],
            alt_weapon_name=weapon_csv.loc[row]["ALT_WEAPON_NAME"],
            weapon_description=weapon_csv.loc[row]["WEAPON_DESCRIPTION"],
        )
        for row in weapon_csv["ID"]
    ]
    Weapon.objects.bulk_create(weapons)
