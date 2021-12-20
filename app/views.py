from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Courses, Books, Videos, Articles
from .forms import CoursesForm, BooksForm, VideosForm, ArticlesForm
from .forms import RegistrationForm, LoginForm


@login_required
def account(request):
	form_book = BooksForm
	form_course = CoursesForm
	username = request.user
	if request.method == 'POST' and 'btn_books' in request.POST:
		form_book = BooksForm(request.POST)
		if form_book.is_valid():
			form_book = form_book.save(commit=False)
			form_book.user = request.user
			form_book.save()
	if request.method == 'POST' and 'btn_courses' in request.POST:
		form_course = CoursesForm(request.POST)
		if form_course.is_valid():
			form_course = form_course.save(commit=False)
			form_course.user = request.user
			form_course.save()
	if request.method == 'POST' and 'delete_book' in request.POST:
		delete_id = request.POST['delete_book']
		print(delete_id)
		Books.objects.filter(id=delete_id).delete()
	if request.method == 'POST' and 'delete_course' in request.POST:
		delete_id = request.POST['delete_course']
		Courses.objects.filter(id=delete_id).delete()
	try:
		books = Books.objects.filter(user=request.user)
	except Books.DoesNotExist:
		books = None
	try:
		courses = Courses.objects.filter(user=request.user)
	except Courses.DoesNotExist:
		courses = None
	print(courses)
	return render(request, 'account.html', {'books': books,
		'courses': courses, 'form_book': form_book,
		'form_course': form_course, 'username': username})

@login_required
def books(request):
	form_book = BooksForm
	username = request.user
	if request.method == 'POST' and 'btn_books' in request.POST:
		form_book = BooksForm(request.POST)
		if form_book.is_valid():
			form_book = form_book.save(commit=False)
			form_book.user = request.user
			form_book.save()
	if request.method == 'POST' and 'delete_book' in request.POST:
		delete_id = request.POST['delete_book']
		print(delete_id)
		Books.objects.filter(id=delete_id).delete()
	try:
		books = Books.objects.filter(user=request.user)
	except Books.DoesNotExist:
		books = None
	return render(request, 'books.html', {'books': books,
		'form_book': form_book,
		'username': username})

@login_required
def courses(request):
	form_course = CoursesForm
	username = request.user
	if request.method == 'POST' and 'btn_courses' in request.POST:
		form_course = CoursesForm(request.POST)
		if form_course.is_valid():
			form_course = form_course.save(commit=False)
			form_course.user = request.user
			form_course.save()
	if request.method == 'POST' and 'delete_course' in request.POST:
		delete_id = request.POST['delete_course']
		Courses.objects.filter(id=delete_id).delete()
	try:
		courses = Courses.objects.filter(user=request.user)
	except Courses.DoesNotExist:
		courses = None
	return render(request, 'courses.html', {'courses': courses, 
		'form_course': form_course, 'username': username})

@login_required
def videos(request):
	form_video = VideosForm
	username = request.user
	if request.method == 'POST' and 'btn_video' in request.POST:
		form_video = VideosForm(request.POST)
		if form_course.is_valid():
			form_video = form_video.save(commit=False)
			form_video.user = request.user
			form_video.save()
	if request.method == 'POST' and 'delete_video' in request.POST:
		delete_id = request.POST['delete_video']
		Videos.objects.filter(id=delete_id).delete()
	try:
		videos = Videos.objects.filter(user=request.user)
	except Courses.DoesNotExist:
		videos = None
	return render(request, 'videos.html', {'videos': videos, 
		'form_video': form_video, 'username': username})

@login_required
def articles(request):
	form_article = ArticlesForm
	username = request.user
	if request.method == 'POST' and 'btn_article' in request.POST:
		form_article = ArticlesForm(request.POST)
		if form_article.is_valid():
			form_article = form_article.save(commit=False)
			form_article.user = request.user
			form_article.save()
	if request.method == 'POST' and 'delete_article' in request.POST:
		delete_id = request.POST['delete_article']
		Articles.objects.filter(id=delete_id).delete()
	try:
		articles = Articles.objects.filter(user=request.user)
	except Articles.DoesNotExist:
		articles = None
	return render(request, 'articles.html', {'articles': articles, 
		'form_article': form_article, 'username': username})

def main(request, username):
	user_exist = User.objects.filter(username=username).exists()
	books = Books.objects.filter(user__username=username)
	courses = Courses.objects.filter(user__username=username)
	return render(request, 'main.html', {'books': books,
		'courses': courses, 'username': username, 'user_exist': user_exist})

def registration(request):
	if request.user.is_authenticated:
		redirect('account')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form = form.save()
			return render(request, 'registration_complete.html', {'form': form})
	form = RegistrationForm()
	return render(request, 'registration.html', {'form': form})

def login_user(request):
	if request.user.is_authenticated:
		return redirect('account')
	errors = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('account')
	form = LoginForm()
	return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
	prev_user = request.user
	logout(request)
	return redirect('main', username=str(prev_user))
