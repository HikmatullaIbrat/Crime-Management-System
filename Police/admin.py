from django.contrib import admin
from .models import Police,PoliceStation,PoliceStationArea
# Register your models here.

admin.site.register(Police)
admin.site.register(PoliceStation)
admin.site.register(PoliceStationArea)