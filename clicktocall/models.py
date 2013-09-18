from django.db import models

# Create your models here.


class Lead(models.Model):
	duration = models.DecimalField(max_digits=5, decimal_places=2)
	from_number = models.IntegerField(max_length=999999999999999)
	to_number = models.IntegerField(max_length=999999999999999)

