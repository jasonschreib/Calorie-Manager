from django.shortcuts import render, redirect
#import authentication and login methods
from django.contrib.auth import authenticate, login, logout
#import the User object
from django.contrib.auth.models import User
# #import the entry class
# from log.models import Entry

# Create your views here.

#splash page view - take in request and render the splash.html template
def splash(request):
  return render(request, 'splash.html', {})

#accounts page view - to signup or login
def accounts(request):
  return render(request, 'accounts.html', {})
