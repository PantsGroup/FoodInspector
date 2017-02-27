from __future__ import unicode_literals

from django.db import models
import re
from django.contrib import messages
from django.utils import timezone
import bcrypt
from datetime import datetime


# class RestaurantManager(models.Manager):

# Create your models here.
class Restaurant(models.Model):
	business_name = models.CharField(max_length=255,unique=True)
	address = models.CharField(max_length=255)
	zip_code = models.CharField(max_length=20)
	inspection_date = models.CharField(max_length=30)
	inspection_score = models.IntegerField()
	violation = models.TextField(max_length=1000)
	risk_category = models.CharField(max_length=100)


class Address(models.Model):
	ID = models.AutoField(primary_key=True)
	business_name = models.CharField(max_length=255)
	address = models.TextField()
	latitude = models.FloatField(max_length=20)
	longitude = models.FloatField(max_length=30)
	latlng = models.CharField(max_length=100,unique=True)
	timestamp = models.DateTimeField(default=timezone.now)
	