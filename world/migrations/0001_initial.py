# Generated by Django 3.1.7 on 2021-08-10 13:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('aircraft', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('hyperlink', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Border1880',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default=1880, max_length=4, verbose_name='year')),
                ('area', models.FloatField()),
                ('name', models.CharField(default='', max_length=40, null=True)),
                ('abbrevname', models.CharField(default='', max_length=12, null=True)),
                ('fips_code', models.CharField(default='', max_length=2, null=True)),
                ('wb_cntry', models.CharField(default='', max_length=3, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Border1914',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default=1914, max_length=4, verbose_name='year')),
                ('area', models.FloatField()),
                ('name', models.CharField(default='', max_length=40, null=True)),
                ('abbrevname', models.CharField(default='', max_length=12, null=True)),
                ('fips_code', models.CharField(default='', max_length=2, null=True)),
                ('wb_cntry', models.CharField(default='', max_length=3, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Border1920',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default=1920, max_length=4, verbose_name='year')),
                ('area', models.FloatField()),
                ('name', models.CharField(default='', max_length=40, null=True)),
                ('abbrevname', models.CharField(default='', max_length=12, null=True)),
                ('fips_code', models.CharField(default='', max_length=2, null=True)),
                ('wb_cntry', models.CharField(default='', max_length=3, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wwi_id', models.IntegerField(verbose_name='WWI_ID')),
                ('msndate', models.CharField(max_length=255, verbose_name='MSNDATE')),
                ('operation', models.CharField(max_length=255, verbose_name='OPERATION')),
                ('country', models.CharField(max_length=255, verbose_name='COUNTRY')),
                ('service', models.CharField(max_length=255, verbose_name='SERVICE')),
                ('unit', models.CharField(max_length=255, verbose_name='UNIT')),
                ('mds', models.CharField(max_length=255, verbose_name='MDS')),
                ('missionnum', models.FloatField(verbose_name='MISSIONNUM')),
                ('departure', models.CharField(max_length=255, verbose_name='DEPARTURE')),
                ('takeofftime', models.CharField(max_length=255, verbose_name='TAKEOFFTIME')),
                ('numberofplanesattacking', models.FloatField(verbose_name='NUMBEROFPLANESATTACKING')),
                ('callsign', models.CharField(max_length=255, verbose_name='CALLSIGN')),
                ('weaponsexpended', models.FloatField(verbose_name='WEAPONSEXPENDED')),
                ('weapontype', models.CharField(max_length=255, verbose_name='WEAPONTYPE')),
                ('weaponweight', models.FloatField(verbose_name='WEAPONWEIGHT')),
                ('bombload', models.FloatField(verbose_name='BOMBLOAD')),
                ('latitude', models.FloatField(verbose_name='LATITUDE')),
                ('longitude', models.FloatField(verbose_name='LONGITUDE')),
                ('tgtlocation', models.CharField(max_length=255, verbose_name='TGTLOCATION')),
                ('tgtcountry', models.CharField(max_length=255, verbose_name='TGTCOUNTRY')),
                ('tgttype', models.CharField(max_length=255, verbose_name='TGTTYPE')),
                ('takeoffbase', models.CharField(max_length=255, verbose_name='TAKEOFFBASE')),
                ('takeofflatitude', models.FloatField(verbose_name='TAKEOFFLATITUDE')),
                ('takeofflongitude', models.FloatField(verbose_name='TAKEOFFLONGITUDE')),
                ('bda', models.CharField(max_length=255, verbose_name='BDA')),
                ('enemyaction', models.CharField(max_length=255, verbose_name='ENEMYACTION')),
                ('routedetails', models.CharField(max_length=255, verbose_name='ROUTEDETAILS')),
                ('isrcollected', models.CharField(max_length=255, verbose_name='ISRCOLLECTED')),
                ('friendlycasualties', models.FloatField(verbose_name='FRIENDLYCASUALTIES')),
                ('friendlycasualties_verbose', models.CharField(max_length=255, verbose_name='FRIENDLYCASUALTIES_VERBOSE')),
                ('weather', models.CharField(max_length=255, verbose_name='WEATHER')),
                ('altitude', models.FloatField(verbose_name='ALTITUDE')),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('weapon_name', models.CharField(max_length=50)),
                ('weapon_type', models.CharField(max_length=50)),
                ('weapon_class', models.CharField(max_length=50)),
                ('nbr_bombs', models.IntegerField()),
                ('alt_weapon_name', models.CharField(max_length=50)),
                ('weapon_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='year')),
                ('area', models.FloatField()),
                ('name', models.CharField(default='', max_length=40, null=True)),
                ('abbrevname', models.CharField(default='', max_length=12, null=True)),
                ('fips_code', models.CharField(default='', max_length=2, null=True)),
                ('wb_cntry', models.CharField(default='', max_length=3, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
