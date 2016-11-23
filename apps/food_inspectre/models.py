from __future__ import unicode_literals

from django.db import models
import re
from django.contrib import messages
import bcrypt
from datetime import datetime


# class RestaurantManager(models.Manager):

# Create your models here.
class Restaurant(models.Model):
	business_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	zip_code = models.CharField(max_length=20)
	inspection_date = models.CharField(max_length=30)
	inspection_score = models.IntegerField()
	violation = models.TextField(max_length=1000)
	risk_category = models.CharField(max_length=100)

	# restMgr = RestaurantManager()