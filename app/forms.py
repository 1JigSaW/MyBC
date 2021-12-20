from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from app.models import Books, Courses, Videos, Articles
from app.models import WantBooks, WantCourses, WantVideos, WantArticles


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

class WantBooksForm(ModelForm):

	class Meta:
		model = WantBooks
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantBooksForm, self).__init__(*args, **kwargs)
		self.fields['author'].widget = forms.TextInput(attrs={
			'class': 'first_field',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field',
			})


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


class WantCoursesForm(ModelForm):
	class Meta:
		model = WantCourses
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantCoursesForm, self).__init__(*args, **kwargs)
		self.fields['place'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})


class VideosForm(ModelForm):
	class Meta:
		model = Videos
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(VideosForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'third_field_2', 'id': 'datepicker_2'})


class WantVideosForm(ModelForm):
	class Meta:
		model = WantVideos
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantVideosForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})


class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(ArticlesForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'third_field_2', 'id': 'datepicker_2'})


class WantArticlesForm(ModelForm):
	class Meta:
		model = WantArticles
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantArticlesForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'first_field_2',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'second_field_2',
			})


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
	