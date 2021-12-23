from django.shortcuts import render, redirect
#import authentication and login methods
from django.contrib.auth import authenticate, login, logout
#import the User object
from django.contrib.auth.models import User
#import the entry class
from log.models import Entry

# Create your views here.

#splash page view - take in request and render the splash.html template
def splash(request):
  return render(request, 'splash.html', {})


#accounts page view - to signup or login
def accounts(request):
  return render(request, 'accounts.html', {})


#homepage view - all of the user's daily logs
def homepage(request):
  print(request.user)
  #if the request is a POST request - meaning new log
  if (request.method == 'POST'):
    print('REQ', request.POST)
    #retrieve data from the post req
    date = request.POST['date']
    breakfast = request.POST['breakfast']
    snackOne = request.POST['snackOne']
    lunch = request.POST['lunch']
    snackTwo = request.POST['snackTwo']
    dinner = request.POST['dinner']
    caloriesBurned = request.POST['caloriesBurned']
    #create a new entry for the database
    Entry.objects.create(date=date, breakfast=breakfast, snackOne=snackOne, lunch=lunch, snackTwo=snackTwo, dinner=dinner, caloriesBurned=caloriesBurned)
  #retrieve all instances of the entries class for this user
  # entries = Entry.objects.filter(author=request.user)
  entries = Entry.objects.all()
  print('entries', entries)
  return render(request, 'homepage.html', {'entries': entries})
