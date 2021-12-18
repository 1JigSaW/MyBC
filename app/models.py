from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Books(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'

	def __str__(self):
		return f'{self.title}'

class Courses(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	place = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'

	def __str__(self):
		return f'{self.title}'

class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	link = models.TextField()
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'

	def __str__(self):
		return f'{self.title}'

class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	link = models.TextField()
	date = models.DateField(default=date.today)

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return f'{self.title}'