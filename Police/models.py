from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

from addresses.models import Address
# Create your models here.

PoliceType = (
    ('PO','Police Officer'),
    ('EC','Entry Clerk')
)
class Police(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE,related_name='police')
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64)
    cantact_number = models.IntegerField()
    police_type  = models.CharField(max_length=16,choices=PoliceType)
    
    def __str__(self):
        return "{first_name}{last_name}".format(
            first_name = self.first_name,
            last_name = self.last_name
        )

class PoliceStation(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='policeStation')
    station_name = models.CharField(max_length=64)
    officer = models.ForeignKey(Police, on_delete=models.CASCADE,null=True, blank=True,related_name='stationOfficer')
    entry_clerk= models.ForeignKey(Police, null=True, blank=True, on_delete=models.CASCADE, related_name='stationClerk')

    def __str__(self):
        return self.station_name

class PoliceStationArea(models.Model):
    police_station = models.ForeignKey(PoliceStation,on_delete=models.CASCADE,related_name='policeStationArea')
    area_name = models.CharField(max_length=64)
    def __str__(self):
        return self.area_name