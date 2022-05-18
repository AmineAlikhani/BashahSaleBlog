from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_sub = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
                                     blank=True)                                      
    def get_url(self):
# the whole args and slug thing
        return reverse('shop:category_selected', args={self.slug})
    def __str__(self):
        return self.name        
                                            
class Product(models.Model):
#related name is refering to??
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    detail = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('shop:product_detail', args={self.slug, })
