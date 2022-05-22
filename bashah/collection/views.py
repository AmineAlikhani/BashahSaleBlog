from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from .models import Collection
# Create your views here.

def collection_view(request, product_id):
	Collection.collect(Collection, product_id)
	collection = Collection.objects.all()
	product = Product.objects.all()
	context = { 'collection' : collection, 'product' : product}
	return render(request, 'collection/collection.html', context)
