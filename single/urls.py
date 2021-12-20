"""single URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('registration/', views.registration, name='registration'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('account/', views.account, name='account'),
	path('account/books/', views.books, name='books'),
	path('account/courses/', views.courses, name='courses'),
	path('account/videos/', views.videos, name='videos'),
	path('account/articles/', views.articles, name='articles'),
	path('account/future_books/', views.want_books, name='future_books'),
	path('account/future_courses/', views.want_courses, name='future_courses'),
	path('account/future_videos/', views.want_videos, name='future_videos'),
	path('account/future_articles/', views.want_articles, name='future_articles'),
	path('<username>/', views.main, name='main'),
]
