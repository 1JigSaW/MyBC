from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from .models import Books
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

	def test_read_task(self):
		self.assertEqual(self.book.user, self.user)
		self.assertEqual(self.book.author, 'Томас Кормен')
		self.assertEqual(self.book.title, 'Алгоритмы: построение и анализ')
		self.assertEqual(self.book.date, self.timestamp + timedelta(days=1))

	def test_update_task_description(self):
		self.book.author = 'Чарльз Эрик Лейзерсон, Клиффорд Штайн'
		self.book.save()
		self.assertEqual(self.book.author, 'Чарльз Эрик Лейзерсон, Клиффорд Штайн')

	def test_update_task_due(self):
		self.book.date = self.timestamp + timedelta(days=2)
		self.book.save()
		self.assertEqual(self.book.date, self.timestamp + timedelta(days=2))
