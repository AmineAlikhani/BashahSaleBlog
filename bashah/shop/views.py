from django.shortcuts import render, get_object_or_404
from shop.models import Product, Category
from django.http import HttpResponse
# Create your views here.

def cat_view(request, slug=None):
	categories = Category.objects.filter(is_sub=False, is_available=True)
	products =  Product.objects.all()
	context ={'categories':categories, 'products':products,}    
	return render(request, 'shop/cat_view.html', context) 
	
def detail(request, slug):
	product = get_object_or_404(Product, slug=slug)
	context = {'product':product}
	return render(request, 'shop/detail.html', context) 
