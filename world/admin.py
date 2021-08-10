from django.contrib.gis  import admin
from .models import Border1880, Border1914, Border1920, WorldBorder, Mission, Aircraft, Weapon

# Register your models here.
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Border1880, admin.OSMGeoAdmin)
admin.site.register(Border1914, admin.OSMGeoAdmin)
admin.site.register(Border1920, admin.OSMGeoAdmin)
admin.site.register(Mission)
admin.site.register(Aircraft)
admin.site.register(Weapon)