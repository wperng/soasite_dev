from django import forms
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    emailTitle = models.CharField(max_length=200, verbose_name="Email Title")
    emailContent = models.CharField(max_length=1000, verbose_name="Email Content")
    startDate = models.DateTimeField(verbose_name="Date Started")
    endDate = models.DateTimeField(null=True, verbose_name="Date Ended")
    isActivate = models.CharField(blank=False, default='Y', max_length=1)

    def __str__(self):
        return self.name


class Signoff(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    soteam = models.CharField(max_length=50, verbose_name="SO Team")
    soby = models.CharField(max_length=100, blank=True, verbose_name="SO By")
    sodate = models.DateTimeField(null=True, verbose_name="SO Date")
    note = models.CharField(max_length=500, blank=True, verbose_name="Note")



