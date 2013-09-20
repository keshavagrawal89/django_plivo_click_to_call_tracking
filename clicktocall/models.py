from django.db import models

# Create your models here.


class Lead(models.Model):
	duration = models.DecimalField(max_digits=5, decimal_places=2)
	from_number = models.BigIntegerField(max_length=999999999999999)
	to_number = models.BigIntegerField(max_length=999999999999999)
#Thinking of some data and tracking?
	date_of_call = models.DateField()

class LeadNumberZones(models.Model):
    	lead_number = models.BigIntegerField(max_length=999999999999999)
    	zone = models.CharField(max_length=50)
