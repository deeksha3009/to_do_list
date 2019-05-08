from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ModelForm
from django import forms


class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000, blank=True)
	date_of_creation = models.DateTimeField(default=datetime.now)
	last_date = models.DateTimeField(default=datetime.now)
	
	complete = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title
