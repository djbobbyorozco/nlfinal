from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Item(models.Model):
	task = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	description = models.CharField(max_length=300)
	date_created = models.DateField(auto_now_add=True)
	completed = models.BooleanField(default=False)		

	def __str__(self):
		return self.description
