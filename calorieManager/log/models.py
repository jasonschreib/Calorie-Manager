from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#model for entries
class Entry(models.Model):
  breakfast = models.IntegerField()
  snackOne = models.IntegerField()
  lunch = models.IntegerField()
  snackTwo = models.IntegerField()
  dinner = models.IntegerField()
  caloriesBurned = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add = True)
  creator = models.ForeignKey(User, on_delete = models.DO_NOTHING)

