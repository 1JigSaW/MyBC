from django.shortcuts import render
from .models import Courses, Books

def main(request):
	books = Books.objects.all()
	courses = Courses.objects.all()
	return render(request, 'main.html', {'books': books,
		'courses': courses})

