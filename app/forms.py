from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from app.models import Books, Courses


class BooksForm(ModelForm):

	class Meta:
		model = Books
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(BooksForm, self).__init__(*args, **kwargs)
		self.fields['author'].widget = forms.TextInput(attrs={
			'class': 'first_field',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field',
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'third_field', 'id': 'datepicker'})


class CoursesForm(ModelForm):
	class Meta:
		model = Courses
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(CoursesForm, self).__init__(*args, **kwargs)
		self.fields['place'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'third_field_2', 'id': 'datepicker_2'})

class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={
			'class': 'username_field_form',
			})
		self.fields['password1'].widget = forms.PasswordInput(attrs={
			'class': 'password_field_form',
			})
		self.fields['email'].widget = forms.EmailInput(attrs={
			'class': 'email_field_form',
			})
		self.fields['password2'].widget = forms.PasswordInput(attrs={
			'class': 'password2_field_form',
			})


class LoginForm(AuthenticationForm):

	class Meta:
		model = User
		fields = ('username', 'password',)
		labels = {
			'username': ('Логин'),
			'password': ('Пароль')
		}

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={
			'class': 'username_field_form',
			})
		self.fields['password'].widget = forms.PasswordInput(attrs={
			'class': 'password_field_form',
			})
	