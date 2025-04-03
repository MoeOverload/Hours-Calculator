from django.contrib import admin

from .models import member, hourssheets, Day, JobSites



admin.site.register(member)

admin.site.register(hourssheets)

admin.site.register(Day)

admin.site.register(JobSites)
