from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Courses, Books
from .forms import CoursesForm, BooksForm, RegistrationForm, LoginForm
from django.contrib.auth import logout, authenticate, login

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

def main(request, username):
	books = Books.objects.filter(user__username=username)
	courses = Courses.objects.filter(user__username=username)
	return render(request, 'main.html', {'books': books,
		'courses': courses, 'username': username})

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
	logout(request)
	return redirect('main', username='wwwwww')
