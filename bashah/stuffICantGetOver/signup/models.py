from django.db import models
#from django.contrib.auth import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Create your models here.

class User(models.User):
	username = models.CharField(max_lenght=190)
	password = ReadOnlyPasswordHashField()
	email = models.CharField(max_lenght = 190, unique=True)



