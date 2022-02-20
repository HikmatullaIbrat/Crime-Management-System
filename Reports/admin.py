from django.contrib import admin

# Register your models here.
from .models import Reporter , Report, Crime, CrimeReport
admin.site.register(Reporter)
admin.site.register(Report)
admin.site.register(Crime)
admin.site.register(CrimeReport)