from django.urls import path
from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.cat_view, name='home'),
#    path('category/<slug:slug>/', views.cat_view, name='category_selected'),
    path('<slug:slug>/', views.detail, name='detail'),
#    path('/', views.detail, name='datail')
]
