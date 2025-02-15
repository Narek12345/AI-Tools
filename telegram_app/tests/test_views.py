from django.test import TestCase

from telegram_app.models import TelegramBot



class TelegramPageTest(TestCase):
	"""Тест домашней страницы Telegram."""


	def test_uses_home_telegram_template(self):
		"""Тест: используется домашний шаблон."""
		response = self.client.get('/telegram/')
		self.assertTemplateUsed(response, 'telegram_app/home_telegram.html')



class ConnectTelegramBotTest(TestCase):
	"""Тест подключения Telegram бота."""


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

		self.assertRedirects(response, f'/telegram/bot/{bot.id}')


	def test_connection_is_successful_with_seccessful_data(self):
		"""Тест: подключение проходит успешно при передаче валидных данных."""
		response = self.client.post(
			'/telegram/connect-bot',
			data={
				'name': 'Telegram bot',
				'token': '8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg',
			}
		)
		self.assertEqual(1, TelegramBot.objects.count())


	def test_for_invalid_input_nothing_saved_to_db(self):
		"""Тест на недопустимый ввод: ничего не сохранится в БД."""
		response = self.client.post(
			'/telegram/connect-bot',
			data={
				'name': '',
				'token': '',
			}
		)
		self.assertEqual(0, TelegramBot.objects.count())


	def test_start_button_view(self):
		"""Тест представления кнопки 'Запустить'."""
		bot = TelegramBot.objects.create(
			name='Telegram bot',
			token='8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg',
		)
		response = self.client.post(
			f'/telegram/bot/start/{bot.id}'
		)

		# Перенаправление на страницу с ботом. Бот запущен.
		self.assertRedirects(response, f'/telegram/bot/{bot.id}')
		bot.refresh_from_db()
		self.assertTrue(bot.is_running)


	# тест ответа бота на интерфейсе сайта.
	# тест ответа бота на интерфейсе telegram.
	# start_bot(request, bot_id): -> при передаче неправильного bot_id появляется страница с 404 / либо предупреждающая страница у вас нет такого бота.



class ShowTelegramBotTest(TestCase):


	def test_show_bot_with_invalid_bot_id(self):
		"""Тест: появляется ошибка 404 при неправильном bot id."""
		response = self.client.get('/telegram/bot/999999')
		self.assertEqual(response.status_code, 404)
