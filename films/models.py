from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length = 30)

	def __repr__(self):
		return f'{self.name}'

	def __str__(self):
		return f'{self.name}'

class Category(models.Model):
	name = models.CharField(max_length = 30)

	def __repr__(self):
		return f'{self.name}'

	def __str__(self):
		return f'{self.name}'


class Director(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)

	def __repr__(self):
		return f'{self.first_name} {self.last_name}'

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Film(models.Model):
	title = models.CharField(max_length = 50)
	release_date = models.TimeField(auto_now=True)
	created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='film_created') 
	available_countries = models.ManyToManyField(Country, related_name='film_availble')
	category = models.ManyToManyField(Category)
	director = models.ManyToManyField(Director)

	def __repr__(self):
		return f'{self.name}'

	def __str__(self):
		return f'{self.title}'




