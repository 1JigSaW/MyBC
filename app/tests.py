from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from .models import Books, Courses
from datetime import date, timedelta

class SigninTest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
		self.user.save()

	def tearDown(self):
		self.user.delete()

	def test_correct(self):
		user = authenticate(username='test', password='12test12')
		self.assertTrue((user is not None) and user.is_authenticated)

	def test_wrong_username(self):
		user = authenticate(username='wrong', password='12test12')
		self.assertFalse(user is not None and user.is_authenticated)

	def test_wrong_pssword(self):
		user = authenticate(username='test', password='wrong')
		self.assertFalse(user is not None and user.is_authenticated)


class BooksTest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
		self.user.save()
		self.timestamp = date.today()
		self.book = Books(user=self.user,
						 author='Томас Кормен',
						 title='Алгоритмы: построение и анализ',
						 date=self.timestamp + timedelta(days=1))
		self.book.save()

	def tearDown(self):
		self.user.delete()

	def test_read_book(self):
		self.assertEqual(self.book.user, self.user)
		self.assertEqual(self.book.author, 'Томас Кормен')
		self.assertEqual(self.book.title, 'Алгоритмы: построение и анализ')
		self.assertEqual(self.book.date, self.timestamp + timedelta(days=1))

	def test_update_book_author(self):
		self.book.author = 'Чарльз Эрик Лейзерсон, Клиффорд Штайн'
		self.book.save()
		self.assertEqual(self.book.author, 'Чарльз Эрик Лейзерсон, Клиффорд Штайн')

	def test_update_book_date(self):
		self.book.date = self.timestamp + timedelta(days=2)
		self.book.save()
		self.assertEqual(self.book.date, self.timestamp + timedelta(days=2))


class CoursesTest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
		self.user.save()
		self.timestamp = date.today()
		self.course = Courses(user=self.user,
						 place='Stepik',
						 title='Алгоритмы',
						 date=self.timestamp + timedelta(days=1))
		self.course.save()

	def tearDown(self):
		self.user.delete()

	def test_read_course(self):
		self.assertEqual(self.course.user, self.user)
		self.assertEqual(self.course.place, 'Stepik')
		self.assertEqual(self.course.title, 'Алгоритмы')
		self.assertEqual(self.course.date, self.timestamp + timedelta(days=1))

	def test_update_course_place(self):
		self.course.author = 'Coursera'
		self.course.save()
		self.assertEqual(self.course.author, 'Coursera')

	def test_wrong_update_course(self):
		self.course.title = 'Selenium'
		self.course.save()
		self.assertNotEqual(self.course.title, 'Seleniumaaaa')

	def test_update_course_date(self):
		self.course.date = self.timestamp + timedelta(days=2)
		self.course.save()
		self.assertEqual(self.course.date, self.timestamp + timedelta(days=2))
