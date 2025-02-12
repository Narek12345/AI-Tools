from django.test import TestCase
from django.core.exceptions import ValidationError

from telegram_app.models import TelegramBot



class TelegramBotModelTest(TestCase):


	def test_cannot_connect_telegram_bot_with_empty_token(self):
		"""Тест: пытается создать обьект с пустым полем token."""
		new_bot = TelegramBot()

		with self.assertRaises(ValidationError):
			new_bot.save()


	def test_duplicate_telegram_bot_are_invalid(self):
		"""Тест: повторы подключения Telegram ботов не допустимы."""
		TelegramBot.objects.create(
			token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
		)

		with self.assertRaises(ValidationError):
			TelegramBot.objects.create(
				token="8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg"
			)
