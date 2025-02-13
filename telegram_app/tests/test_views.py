from django.test import TestCase



class TelegramPageTest(TestCase):
	"""Тест домашней страницы telegram."""


	def test_uses_home_telegram_template(self):
		"""Тест: используется домашний шаблон."""
		response = self.client.get('/telegram/')
		self.assertTemplateUsed(response, 'telegram_app/home_telegram.html')


	def test_connect_telegram_bot(self):
		"""Тест: подключение нового telegram bot."""
		response = self.client.get('/telegram/connect-bot')
		self.assertTemplateUsed(response, 'telegram_app/connect_bot.html')
