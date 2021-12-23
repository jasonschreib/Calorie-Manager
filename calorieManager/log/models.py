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
  # creator = models.ForeignKey(User, on_delete = models.DO_NOTHING)


  #return debugging representation of the object
  def __repr__(self):
    return "Entry({}, {}, {}, {}, {}, {}, {})".format(self.breakfast, self.snackOne, self.lunch, self.snackTwo, self.dinner, self.caloriesBurned, self.timestamp)

  #return readable representation of the object - display to end user
  def __str__(self):
    total = self.breakfast + self.snackOne + self.lunch + self.snackTwo + self.dinner + self.caloriesBurned + self.timestamp
    return '{} - {}'.format(total, self.caloriesBurned)