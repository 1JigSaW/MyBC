from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.db.models import Q
from .models import Courses, Books, Videos, Articles
from .models import WantCourses, WantBooks, WantVideos, WantArticles
from .forms import CoursesForm, BooksForm, VideosForm, ArticlesForm
from .forms import RegistrationForm, LoginForm
from .forms import WantCoursesForm, WantBooksForm, WantVideosForm, WantArticlesForm


# @login_required
# def account(request):
# 	username = request.user
# 	count_books = Books.objects.filter(user=username).count()
# 	count_courses = Courses.objects.filter(user=username).count()
# 	count_articles = Articles.objects.filter(user=username).count()
# 	count_videos = Videos.objects.filter(user=username).count()
# 	last_book = Books.objects.latest('date')
# 	last_course = Courses.objects.latest('date')
# 	last_article = Articles.objects.latest('date')
# 	last_video = Videos.objects.latest('date')
# 	return render(request, 'account.html', {'username': username,
# 		'count_books': count_books, 'count_courses': count_courses, 
# 		'count_articles': count_articles, 'count_videos': count_videos,
# 		'last_book': last_book, 'last_course': last_course,
# 		'last_article': last_article, 'last_video': last_video})

def account(request):
	username = 'wwwwww'
	if request.user.is_authenticated:
		username = request.user
	username = User.objects.get(username=username)
	count_books = Books.objects.filter(user=username).count()
	count_courses = Courses.objects.filter(user=username).count()
	count_articles = Articles.objects.filter(user=username).count()
	count_videos = Videos.objects.filter(user=username).count()
	last_book = Books.objects.latest('date')
	last_course = Courses.objects.latest('date')
	last_article = Articles.objects.latest('date')
	last_video = Videos.objects.latest('date')
	return render(request, 'account.html', {'username': username,
		'count_books': count_books, 'count_courses': count_courses, 
		'count_articles': count_articles, 'count_videos': count_videos,
		'last_book': last_book, 'last_course': last_course,
		'last_article': last_article, 'last_video': last_video})

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
			form_book = BooksForm()
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
def want_books(request):
	form_want_book = WantBooksForm
	username = request.user
	if request.method == 'POST' and 'btn_books' in request.POST:
		form_want_book = WantBooksForm(request.POST)
		if form_want_book.is_valid():
			form_want_book = form_want_book.save(commit=False)
			form_want_book.user = request.user
			form_want_book.save()
			form_book = WantBooksForm()
	if request.method == 'POST' and 'delete_book' in request.POST:
		delete_id = request.POST['delete_book']
		print(delete_id)
		WantBooks.objects.filter(id=delete_id).delete()
	try:
		want_books = WantBooks.objects.filter(user=request.user)
	except WantBooks.DoesNotExist:
		want_books = None
	return render(request, 'want_books.html', {'want_books': want_books,
		'form_want_book': form_want_book,
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
			form_book = CoursesForm()
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
def want_courses(request):
	form_want_course = WantCoursesForm
	username = request.user
	if request.method == 'POST' and 'btn_courses' in request.POST:
		form_want_course = WantCoursesForm(request.POST)
		if form_want_course.is_valid():
			form_want_course = form_want_course.save(commit=False)
			form_want_course.user = request.user
			form_want_course.save()
			form_want_course = WantCoursesForm()
	if request.method == 'POST' and 'delete_course' in request.POST:
		delete_id = request.POST['delete_course']
		WantCourses.objects.filter(id=delete_id).delete()
	try:
		want_courses = WantCourses.objects.filter(user=request.user)
	except Courses.DoesNotExist:
		want_courses = None
	return render(request, 'want_courses.html', {'want_courses': want_courses, 
		'form_want_course': form_want_course, 'username': username})

@login_required
def videos(request):
	form_video = VideosForm
	username = request.user
	if request.method == 'POST' and 'btn_videos' in request.POST:
		form_video = VideosForm(request.POST)
		if form_video.is_valid():
			form_video = form_video.save(commit=False)
			form_video.user = request.user
			form_video.save()
			form_video = VideosForm()
	if request.method == 'POST' and 'delete_video' in request.POST:
		delete_id = request.POST['delete_video']
		Videos.objects.filter(id=delete_id).delete()
	try:
		videos = Videos.objects.filter(user=request.user)
	except Videos.DoesNotExist:
		videos = None
	return render(request, 'videos.html', {'videos': videos, 
		'form_video': form_video, 'username': username})

@login_required
def want_videos(request):
	form_want_video = WantVideosForm
	username = request.user
	if request.method == 'POST' and 'btn_videos' in request.POST:
		form_want_video = WantVideosForm(request.POST)
		if form_want_video.is_valid():
			form_want_video = form_want_video.save(commit=False)
			form_want_video.user = request.user
			form_want_video.save()
			form_want_video = WantVideosForm()
	if request.method == 'POST' and 'delete_video' in request.POST:
		delete_id = request.POST['delete_video']
		WantVideos.objects.filter(id=delete_id).delete()
	try:
		want_videos = WantVideos.objects.filter(user=request.user)
	except WantVideos.DoesNotExist:
		want_videos = None
	return render(request, 'want_videos.html', {'want_videos': want_videos, 
		'form_want_video': form_want_video, 'username': username})

@login_required
def articles(request):
	form_article = ArticlesForm
	username = request.user
	if request.method == 'POST' and 'btn_articles' in request.POST:
		form_article = ArticlesForm(request.POST)
		if form_article.is_valid():
			form_article = form_article.save(commit=False)
			form_article.user = request.user
			form_article.save()
			form_article = ArticlesForm()
	if request.method == 'POST' and 'delete_article' in request.POST:
		delete_id = request.POST['delete_article']
		Articles.objects.filter(id=delete_id).delete()
	try:
		articles = Articles.objects.filter(user=request.user)
	except Articles.DoesNotExist:
		articles = None
	return render(request, 'articles.html', {'articles': articles, 
		'form_article': form_article, 'username': username})

@login_required
def want_articles(request):
	form_want_article = WantArticlesForm
	username = request.user
	if request.method == 'POST' and 'btn_articles' in request.POST:
		form_want_article = WantArticlesForm(request.POST)
		if form_want_article.is_valid():
			form_want_article = form_want_article.save(commit=False)
			form_want_article.user = request.user
			form_want_article.save()
			form_want_article = WantArticlesForm()
	if request.method == 'POST' and 'delete_article' in request.POST:
		delete_id = request.POST['delete_article']
		WantArticles.objects.filter(id=delete_id).delete()
	try:
		want_articles = WantArticles.objects.filter(user=request.user)
	except WantArticles.DoesNotExist:
		want_articles = None
	return render(request, 'want_articles.html', {'want_articles': want_articles, 
		'form_want_article': form_want_article, 'username': username})

# def main(request, username):
# 	user_exist = User.objects.filter(username=username).exists()
# 	books = Books.objects.filter(user__username=username)
# 	courses = Courses.objects.filter(user__username=username)
# 	return render(request, 'main.html', {'books': books,
# 		'courses': courses, 'username': username, 'user_exist': user_exist})

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
	return redirect('account')

def search(request):
	user_stat = []
	if 'q' in request.GET and request.GET['q']:
		query = request.GET.get('q')
		user_list = User.objects.filter(Q(username__icontains=query))
		for user in user_list:
			books_count = Books.objects.filter(user=user).count()
			courses_count = Courses.objects.filter(user=user).count()
			articles_count = Articles.objects.filter(user=user).count()
			videos_count = Videos.objects.filter(user=user).count()
			user_stat.append({ 'user': user, 'books_count': books_count, 
				'courses_count': courses_count, 'articles_count': articles_count, 
				'videos_count': videos_count}) 
		return render(request, 'search.html', {'user_stat': user_stat})