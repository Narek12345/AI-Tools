from django.test import TestCase
from django.core.exceptions import ValidationError

from telegram_app.models import TelegramBot



class TelegramBotModelTest(TestCase):


	def test_connect_bot_with_empty_token(self):
		"""Тест: пытается создать обьект с пустым полем token."""
		new_bot = TelegramBot()

		with self.assertRaises(ValidationError):
			new_bot.full_clean()
			new_bot.save()
