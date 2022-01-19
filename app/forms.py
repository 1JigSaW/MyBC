from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
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
			'class': 'form-control', 'placeholder': 'Автор'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название'
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата'})

class WantBooksForm(ModelForm):

	class Meta:
		model = WantBooks
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantBooksForm, self).__init__(*args, **kwargs)
		self.fields['author'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Автор'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Автор'
			})


class CoursesForm(ModelForm):
	class Meta:
		model = Courses
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(CoursesForm, self).__init__(*args, **kwargs)
		self.fields['place'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Платформа'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название'
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'})


class WantCoursesForm(ModelForm):
	class Meta:
		model = WantCourses
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantCoursesForm, self).__init__(*args, **kwargs)
		self.fields['place'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Платформа'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название'
			})


class VideosForm(ModelForm):
	class Meta:
		model = Videos
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(VideosForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Ссылка'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название',
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'})


class WantVideosForm(ModelForm):
	class Meta:
		model = WantVideos
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantVideosForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Ссылка',
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название',
			})


class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(ArticlesForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Ссылка'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название'
			})
		self.fields['date'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'})


class WantArticlesForm(ModelForm):
	class Meta:
		model = WantArticles
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(WantArticlesForm, self).__init__(*args, **kwargs)
		self.fields['link'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Ссылка'
			})
		self.fields['title'].widget = forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Название'
			})


class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Введите логин'
			})
		self.fields['password1'].widget = forms.PasswordInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Введите пароль'
			})
		self.fields['email'].widget = forms.EmailInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Введите email'
			})
		self.fields['password2'].widget = forms.PasswordInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Повторите пароль'
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
			'class': 'form-control text-center', 'placeholder': 'Введите логин'
			})
		self.fields['password'].widget = forms.PasswordInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Введите пароль'
			})

class MyPasswordResetForm(PasswordResetForm):

	class Meta:
			model = User
			fields = ('email',)
			labels = {
				'email': ('Email'),
			}

	def __init__(self, *args, **kwargs):
		super(MyPasswordResetForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(attrs={
			'class': 'form-control text-center', 'placeholder': 'Введите почту'
			})