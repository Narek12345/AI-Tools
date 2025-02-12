from django.test import TestCase



class TelegramPageTest(TestCase):
	"""Тест домашней страницы telegram."""


	def test_uses_home_telegram_template(self):
		"""Тест: используется домашний шаблон."""
		response = self.client.get('/telegram')
		self.assertTemplateUsed(response, 'telegram_app/home_telegram.html')
