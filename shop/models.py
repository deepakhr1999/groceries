from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Item(models.Model):
	title = models.CharField(max_length = 100)
	price = models.IntegerField()
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	description = models.TextField(default = '')

	def __str__(self):
		return self.title

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	isDelivered = models.BooleanField(default = False)
	
	def __str__(self):
		return f"{item} x {quantity} for {user.username}"

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	items = models.ManyToManyField(Order)

	def __str__(self):
		return self.user.username+"'s Cart"
