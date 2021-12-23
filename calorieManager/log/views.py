from django.shortcuts import render, redirect
#import authentication and login methods
from django.contrib.auth import authenticate, login, logout
#import the User object
from django.contrib.auth.models import User
#import the entry class
from log.models import Entry
#import time to fulfill first-party package req.
import time
#import faker
from faker import Faker
fake = Faker()

# Create your views here.

#splash page view - take in request and render the splash.html template
def splash(request):
  #create a random name for requirements
  name = fake.name()
  print('NAME', name)
  sentence = fake.sentence()
  from emoji import emojize
  emoji = emojize(":thumbs_up:")
  return render(request, 'splash.html', {'randomName': name, 'randomSentence': sentence, 'emoji': emoji})


#accounts page view - to signup or login
def accounts(request):
  return render(request, 'accounts.html', {})


#homepage view - all of the user's daily logs
def homepage(request):
  currtime = time.strftime("%d:%m:%y",time.localtime(time.time()))
  print(currtime)
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
  return render(request, 'homepage.html', {'entries': entries, 'currtime': currtime})


#sign up page view - will always redirect to either accounts (if can't go through) or home
def signup(request):
  #if the request is POST
  if (request.method == 'POST'):
    #get the username, email, password from the request
    username, email, password = request.POST['username'], request.POST['email'], request.POST['password']
    #create a user with the username, email, password
    user = User.objects.create_user(username=username, email=email, password=password)
    print('USER', user)
    #login the user
    login(request, user)
    #return a redirect to user's homepage
    return redirect('/homepage')


#login page view - will always redirect to either accounts (if can't go through) or home
def log_in(request):
  #if the user is authenticated
  if (request.user.is_authenticated):
    #bring them to their homepage
    return redirect('/homepage')
  #if we are making a post request --> creating a new session
  if (request.method == 'POST'):
    #get username and password
    username, password = request.POST['username'], request.POST['password']
    #authenticate the user
    user = authenticate(username=username, password=password)
    #if the user is not authenticated
    if (user is None):
      #return back to the login page
      return redirect('/accounts')
    #otherwise if the user is a user
    else:
      #login the user
      login(request, user)
      #redirect to homepage
      return redirect('/homepage')


#edit page view - page to edit a specific entry
def edit(request):
  print('REq', request.GET)
  #if the request is a POST request - meaning new log
  if (request.method == 'POST'):
    #get the entry to update - currently running into a bug with the id
    entry = Entry.objects.get(id=request.GET['id'])
    print('after')
    #get the updated info
    date = request.POST['date']
    breakfast = request.POST['breakfast']
    snackOne = request.POST['snackOne']
    lunch = request.POST['lunch']
    snackTwo = request.POST['snackTwo']
    dinner = request.POST['dinner']
    caloriesBurned = request.POST['caloriesBurned']
    #save the updates
    entry.save(date=date, breakfast=breakfast, snackOne=snackOne, lunch=lunch, snackTwo=snackTwo, dinner=dinner, caloriesBurned=caloriesBurned)
    #redirect back to the homepage
    return redirect('homepage')
  return render(request, 'edit.html', {})


#delete page view - redirects to homepage after deleting a tweet
def delete(request):
  #retrieve the entry to delete
  entry = Entry.objects.get(id=request.GET['id'])
  #delete the entry
  entry.delete()
  print('hit the delete route')
  #redirect back to the homepage
  return redirect('homepage')


#logout page view - will logout user and redirect to the accounts page
def logout_view(request):
  logout(request)
  return redirect('accounts')