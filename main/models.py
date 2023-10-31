from django.db import models
from django.contrib.auth.models import User

class Videos(models.Model):
	title = models.CharField(max_length=64)
	file = models.FileField(upload_to='videos/')
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'

class Category(models.Model):
	name = models.CharField(max_length=64, db_index=True)

	def __str__(self):
		return f'{self.name}'