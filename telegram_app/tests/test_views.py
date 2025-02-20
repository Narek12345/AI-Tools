import os

from django.test import TestCase

from telegram_app.models import TelegramBot, TelegramBotStatus


TEST_TELEGRAM_BOT_TOKEN = os.getenv("TEST_TELEGRAM_BOT_TOKEN")



class TelegramPageTest(TestCase):
	"""Тест домашней страницы Telegram."""


	def test_uses_home_telegram_template(self):
		"""Тест: используется домашний шаблон."""
		response = self.client.get('/telegram/')
		self.assertTemplateUsed(response, 'telegram_app/home_telegram.html')



class ConnectTelegramBotTest(TestCase):
	"""Тест подключения Telegram бота."""


	def test_connect_telegram_bot_template(self):
		"""Тест: подключение нового telegram bot."""
		response = self.client.get('/telegram/connect-bot')
		self.assertTemplateUsed(response, 'telegram_app/connect_bot.html')


	def test_redirect_to_bot_page_after_successful_connection(self):
		"""Тест: перенаправление на страницу бота после успешного подключения."""
		response = self.client.post(
			'/telegram/connect-bot',
			data={
				'name': 'Telegram bot',
				'token': TEST_TELEGRAM_BOT_TOKEN,
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
				'token': TEST_TELEGRAM_BOT_TOKEN,
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



class ShowTelegramBotTest(TestCase):
	"""Тест: страница с конкретным Telegram ботом."""


	def test_uses_bot_template(self):
		"""Тест: используется шаблон бота с его информацией."""
		bot = TelegramBot.objects.create(
			name='Telegram bot',
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		response = self.client.get(f'/telegram/bot/{bot.id}')
		self.assertTemplateUsed(response, 'telegram_app/bot_page.html')


	def test_view_show_bot_with_invalid_bot_id(self):
		"""Тест: появляется ошибка 404 при неправильном bot id для представления show_bot."""
		response = self.client.get('/telegram/bot/999999')
		self.assertEqual(response.status_code, 404)


	def test_in_response_receives_bot_instance_and_status(self):
		"""Тест: в ответ на запрос принимаем экземпляр бота и его статус."""
		bot = TelegramBot.objects.create(
			name='Telegram bot',
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		bot_status = TelegramBotStatus.objects.get(bot=bot)

		response = self.client.get(f'/telegram/bot/{bot.id}')
		bot_from_response = response.context['bot']
		bot_status_from_response = response.context['bot_status']

		self.assertEqual(bot, bot_from_response)
		self.assertEqual(bot_status, bot_status_from_response)




class StartTelegramBotTest(TestCase):
	"""Тест: запуск Telegram бота."""


	def test_redirect_after_clicking_start_button(self):
		"""Тест: перенаправление после нажатия кнопки 'Запустить'."""
		bot = TelegramBot.objects.create(
			name='Telegram bot',
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		response = self.client.get(f'/telegram/bot/start/{bot.id}')
		self.assertRedirects(response, f'/telegram/bot/{bot.id}')


	def test_start_button_view(self):
		"""Тест представления кнопки 'Запустить'."""
		bot = TelegramBot.objects.create(
			name='Telegram bot',
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		response = self.client.post(
			f'/telegram/bot/start/{bot.id}'
		)

		# Перенаправление на страницу с ботом. Бот запущен.
		self.assertRedirects(response, f'/telegram/bot/{bot.id}')
		bot.refresh_from_db()
		self.assertTrue(bot.is_running)


	def test_view_start_bot_with_invalid_bot_id(self):
		"""Тест: появляется ошибка 404 при неправильном bot id для представления start_bot."""
		response = self.client.get('/telegra/bot/999999')
		self.assertEqual(response.status_code, 404)
