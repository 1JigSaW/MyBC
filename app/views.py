from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Courses, Books
from .forms import CoursesForm, BooksForm, RegistrationForm

@login_required
def main(request):
	form_book = BooksForm
	form_course = CoursesForm
	books = Books.objects.all()
	courses = Courses.objects.all()
	if request.method == 'POST' and 'btn_books' in request.POST:
		form_book = BooksForm(request.POST)
		if form_book.is_valid():
			form_book = form_book.save()
	if request.method == 'POST' and 'btn_courses' in request.POST:
		form_course = CoursesForm(request.POST)
		if form_course.is_valid():
			form_course = form_course.save()
	if request.method == 'POST' and 'delete_book' in request.POST:
		delete_id = request.POST['delete_book']
		Books.objects.filter(id=delete_id).delete()
	if request.method == 'POST' and 'delete_course' in request.POST:
		delete_id = request.POST['delete_course']
		Courses.objects.filter(id=delete_id).delete()
	return render(request, 'main.html', {'books': books,
		'courses': courses, 'form_book': form_book,
		'form_course': form_course})

def account(request, username):
	books = Books.objects.all()
	courses = Courses.objects.all()
	return render(request, 'account.html', {'books': books,
		'courses': courses})

def registration(request):
	if request.user.is_authenticated:
		redirect('main')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		print('123')
		if form.is_valid():
			form = form.save()
			print('1234')
			return render(request, 'registration_complete.html', {'form': form})
	form = RegistrationForm()
	return render(request, 'registration.html', {'form': form})

