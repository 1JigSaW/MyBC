from django.db import models
from datetime import date


class Books(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'

	def __str__(self):
		return f'{self.title}'

class Courses(models.Model):
	place = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'

	def __str__(self):
		return f'{self.title}'

