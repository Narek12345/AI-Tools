from django.test import TestCase



class TelegramPageTest(TestCase):
	"""Тест домашней страницы telegram."""


	def test_uses_home_telegram_template(self):
		"""Тест: используется домашний шаблон."""
		response = self.client.get('/telegram/')
		self.assertTemplateUsed(response, 'telegram_app/home_telegram.html')



class ConnectTelegramBotTest(TestCase):


	def test_connect_telegram_bot(self):
		"""Тест: подключение нового telegram bot."""
		response = self.client.get('/telegram/connect-bot')
		self.assertTemplateUsed(response, 'telegram_app/connect_bot.html')


	def test_bot_connection_page(self):
		"""Тест: перенаправление на страницу бота после успешного подключения."""
		response = self.client.post(
			'/telegram/connect-bot',
			data={
				'name': 'Telegram bot',
				'token': '8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg',
			}
		)
		bot = TelegramBot.objects.first()

		self.assertRedirect(response, f'/telegram/bot/{bot.id}')
