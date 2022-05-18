from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse
from user.forms import UserCreationForm, SignUpForm
from .models import user
# Create your views here.

def index(request):
	return HttpResponse(f"well done")  
		     

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponse(f"Fuck me, {user.username} is in")       
           # return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
