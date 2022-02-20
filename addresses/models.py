from django.db import models

# Create your models here.
class Address(models.Model):
    province = models.CharField(max_length=64)
    village  = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    home_number = models.CharField(max_length=64)
    
    def __str__(self):
        return "{district}\n{province}".format(
            district = self.district,
            province = self.province,
        )
    def get_address(self):
        return "{home_number}\n{village}\n{district}\n{province}".format(
            home= self.home_number,
            village= self.village,
            district = self.district,
            province = self.province,
        )