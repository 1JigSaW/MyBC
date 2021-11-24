from django.shortcuts import render
from .models import Courses, Books
from .forms import CoursesForm, BooksForm

def main(request):
	if request.method == 'POST' and 'btn_books' in request.POST:
		form_book = BooksForm(request.POST)
		if form_book.is_valid():
			form_book = form_book.save()
	if request.method == 'POST' and 'btn_courses' in request.POST:
		form_course = CoursesForm(request.POST)
		if form_course.is_valid():
			form_course = form_course.save()
	form_book = BooksForm
	form_course = CoursesForm
	books = Books.objects.all()
	courses = Courses.objects.all()
	return render(request, 'main.html', {'books': books,
		'courses': courses, 'form_book': form_book,
		'form_course': form_course})

