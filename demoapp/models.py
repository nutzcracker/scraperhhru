from django.db import models
from django.utils import timezone

class Widget(models.Model):
    name = models.CharField(max_length=140)



class Job(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
   
    class Admin:
        pass
