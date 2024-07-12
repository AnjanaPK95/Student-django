from django.db import models

# Create your models here.
class Students(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    rollNbr = models.IntegerField()
    standard = models.CharField(max_length=50)