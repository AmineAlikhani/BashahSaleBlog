from django.urls import path
from collection import views

app_name = 'collection'

urlpatterns = [
    path('<int:product_id>/', views.collection_view, name='collect'),
#    path('category/<slug:slug>/', views.home, name='category_filter'),
#    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
