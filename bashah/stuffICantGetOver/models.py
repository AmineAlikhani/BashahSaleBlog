#!usr/bin/python
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Create your models here.

class user(models.Model):
	name = models.OneToOneField(User, on_delete=models.CASCADE)
	password = ReadOnlyPasswordHashField()
	def __str__(self):
		return f"{self.name}"


