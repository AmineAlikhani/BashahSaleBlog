from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.http import HttpResponse

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		    form.save()
		    username = form.cleand_data.get('username')
		    raw_password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=raw_password)
		    request = 'GET'
		    form.save()
		    login(request, user)
		return HttpResponse(f"Signed up! {username} ")
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form':form})
'''	
def signin(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid:
			return HttpResponce('you are in!')
			'''
