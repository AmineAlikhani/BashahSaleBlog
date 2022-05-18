from django.urls import path, re_path
from django.conf.urls import include
from . import views

app_name = "user"

urlpatterns = [
#	re_path('', views.dashboard, name='dashboard'),
	path('accounts/index/', views.index, name='index'),
	re_path(r'^accounts/', include('django.contrib.auth.urls')),
	re_path(r'^register/', views.signup, name='register'),
]

