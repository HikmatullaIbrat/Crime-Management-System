from addresses.models import Address
from django.db import models

# Create your models here.

ReportType = (
    ('Crime','crime'),
    ('Missing Person','missing person')
)
CrimeStatus = (
    ('Wanted','wanted'),
    ('Arrested','arrested')
)
MissingPersonStatus = (
    ('Founded','founded'),
    ('Still Missing','still missing'),
)
class Reporter(models.Model):
    reporter_name   = models.CharField(max_length=64)
    contact_number  = models.CharField(max_length=10)

    def __str__(self):
        return self.reporter_name

class Report(models.Model):
    Reporter        = models.ForeignKey(Reporter, related_name='Reporter',on_delete=models.CASCADE)
    date            = models.DateTimeField(auto_now_add=True)
    report_type     = models.CharField(max_length=16, choices=ReportType)
    location        = models.CharField(max_length=64)
    
    def __str__(self):
        return self.report_type

class Crime(models.Model):
    crime_Name      = models.CharField(max_length=64)
    report          = models.ManyToManyField('Report',through='CrimeReport')

    def __str__(self):
        return self.crime_Name
class CrimeReport(models.Model):
    Description     = models.TextField(max_length=364 ,null=True, blank=True)
    crime_status = models.CharField(max_length=32, choices=CrimeStatus)
    crime   = models.ForeignKey(Crime,on_delete=models.CASCADE,related_name='crimes')
    image           = models.ImageField(null=True,blank=True)
    report  = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='reports')
    

    def __str__(self):
        return self.report
    
class MissingPerson(models.Model):
    Person_Name = models.CharField(max_length=64)
    Description     = models.TextField(max_length=364, null=True, blank=True)
    address     = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='missing_address')
    Report      = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='missing_person_report')
    status      = models.CharField(max_length=32, choices=MissingPersonStatus)
    image           = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.Person_Name
    
    
