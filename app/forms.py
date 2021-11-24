from django.forms import ModelForm
from django import forms
from app.models import Books, Courses

class BooksForm(ModelForm):
	class Meta:
		model = Books
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(BooksForm, self).__init__(*args, **kwargs)
		self.fields['author'].widget = forms.TextInput(attrs={
			'class': 'first_field',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field',
			})
		self.fields['date'].widget = forms.DateInput(attrs={
			'class': 'third_field',
			})


class CoursesForm(ModelForm):
	class Meta:
		model = Courses
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CoursesForm, self).__init__(*args, **kwargs)
		self.fields['place'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})
		self.fields['date'].widget = forms.DateInput(attrs={
			'class': 'third_field_2',
			})