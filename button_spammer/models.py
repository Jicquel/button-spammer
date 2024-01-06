from django.db import models

# Create your models here.

class Action(models.Model):
    action_name = models.CharField(max_length=200, primary_key=True)

class Occurence(models.Model):
    action_name = models.ForeignKey(Action, on_delete=models.CASCADE)
    occurence_date = models.DateTimeField("date field", auto_now_add=True)