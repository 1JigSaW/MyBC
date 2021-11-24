from django.forms import ModelForm
from django import forms
from app.models import Books, Courses

class BooksForm(ModelForm):
	class Meta:
		model = Books
		fields = '__all__'


class CoursesForm(ModelForm):
	class Meta:
		model = Courses
		fields = '__all__'