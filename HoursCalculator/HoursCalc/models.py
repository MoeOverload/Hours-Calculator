from django.db import models


class JobSites(models.Model):
    SiteName = models.CharField(max_length=30)
    SiteAddress= models.CharField


class Day(models.Model):
    Date = models.DateField(name="Date")
    JobName = models.ManyToManyField(
        JobSites    
    )
    StartTime = models.TimeField(name="StartTime")
    Endtime = models.TimeField(name="EndTime")
    BreakTime = models.TimeField(name="BreakTime")
    HoursTotal = models.IntegerField(name="TotalHours")

class hourssheets(models.Model):
    StartDate = models.DateField(name="StartDate")
    EndDate = models.DateField(name="EndDate")
    Days = models.ManyToManyField(
        Day
    )
class member(models.Model):
    Email = models.EmailField()
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=12)
    HoursSheets = models.ManyToManyField(
        hourssheets
        )
    Jobnames = models.ManyToManyField(
        JobSites
    )


