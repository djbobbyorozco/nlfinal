from rest_framework import serializers
from .models import ToDoList, Item

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDoList
		fields = ('id', 'user', 'name')

class ItemSerializer(serializers.ModelSerializers):
	class Meta:
		model = Item
		fields = ('task', 'description', 'date_created', 'completed')	