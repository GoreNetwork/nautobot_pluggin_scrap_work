
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

from nautobot.core.models import BaseModel


class MaintenanceNotice(BaseModel):
    UserModel = get_user_model()  #Pulling users from Nautobot
    start_time = models.DateTimeField() #When is the maintenance starting
    end_time = models.DateTimeField(editable=False) #Calculated when it will end.  This isn't editable
    duration = models.PositiveSmallIntegerField(help_text="Duration (in minutes)") # How long will it go
    comments = models.CharField(blank=True, max_length=200)#Short comments people can make
    created_by = models.ForeignKey(
        to=UserModel, on_delete=models.SET_NULL, blank=True, null=True, editable=False
    ) #Foreign key to the django's User model
    devices = models.ManyToManyField(
        to="dcim.Device", related_name="maintenance_notices"
    ) #Foreign key part of the dcim "table/db?" The related_name gives a way for the assocation to be followed in the opsite direction
        # Because 1 notice may hit many devices this is a ManyToMany

    class Meta: #Just a bunch of meta data
        ordering = ("start_time", "pk") #Order them by start time rather than the random ID field that is generated
        # and how they would be ordered normally
        verbose_name = "Maintenance Notice"
        verbose_name_plural = "Maintenance Notices"

    def __str__(self):
        #Figures out what the model should look like if you call it as a string EX: print (instance)
            #print(MaintenanceNotice.objects.first()) would print
                #2022-04-22 00:00 (60 minutes)
        return f"{self.start_time:%Y-%m-%d %H:%M} ({self.duration} minutes)"

    def get_absolute_url(self):

        """Return absolute URL for instance."""
        return reverse("plugins:maintenance_notices:maintenancenotice", args=[self.pk])

    def save(self, *args, **kwargs):
        #Overide built in save to figure out the end_time columb (the uneditable one)
        self.end_time = self.start_time + timedelta(minutes=self.duration)
        super().save(*args, **kwargs) 