from django.db import models
from django.db.models.base import Model

# https://docs.google.com/document/d/1iyVRVTjwbguB_YkJxLIGPPRCIyo-MmCW1_DkIplCrQU/edit?usp=sharing

class Event(models.Model):
    event_name = models.CharField(max_length=70)
    data = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name + ' - ' + self.location
