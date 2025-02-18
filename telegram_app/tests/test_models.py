from django.test import TestCase
from django.core.exceptions import ValidationError

from telegram_app.models import TelegramBot, TelegramBotStatus



class TelegramBotModelTest(TestCase):


	def test_cannot_connect_telegram_bot_with_empty_token(self):
		"""Тест: пытается создать обьект с пустым полем token."""
		new_bot = TelegramBot()

		with self.assertRaises(ValidationError):
			new_bot.save()


	def test_duplicate_telegram_bot_are_invalid(self):
		"""Тест: повторы подключения Telegram ботов не допустимы."""
		TelegramBot.objects.create(
			name="Bot1",
			token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
		)

		with self.assertRaises(ValidationError):
			TelegramBot.objects.create(
				name="Bot2",
				token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
			)


	def test_by_default_is_running_is_False(self):
		bot = TelegramBot.objects.create(
			name="Bot1",
			token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
		)
		self.assertFalse(bot.is_running)



class TelegramBotStatusModelTest(TestCase):


	def test_bot_status_is_updated_when_is_running_is_updated(self):
		bot = TelegramBot.objects.create(
			name="Bot1",
			token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
		)
		bot.is_running = True
		bot.save()

		bot_status = TelegramBotStatus.objects.get(bot=bot)
		self.assertTrue(bot_status.is_running)
