from django.db import models
from shop.models import Product

# Create your models here.

class Collection(models.Model):
	product_ids = models.IntegerField()
	def collect(self,product_id):
		try:
			collection = self.objects.get(product_ids=product_id)
		except self.DoesNotExist:
			collection = self(product_ids=product_id)
			collection.save()
	def __int__(self):
		return self.product_ids


