from .views import AircraftList, MissionList, WeaponList, WorldBorderList
from django.urls import path

urlpatterns = [
    path('borders/', WorldBorderList.as_view(), name='borders'),
    path('missions/', MissionList.as_view(), name='missions'),
    path('weapons/', WeaponList.as_view(), name='weapons'),
    path('aircraft/', AircraftList.as_view(), name='aircraft'),
]
