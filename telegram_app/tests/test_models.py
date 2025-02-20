import os

from django.test import TestCase
from django.core.exceptions import ValidationError

from datetime import datetime, timedelta

from telegram_app.models import TelegramBot, TelegramBotStatus


TEST_TELEGRAM_BOT_TOKEN = os.getenv("TEST_TELEGRAM_BOT_TOKEN")



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
			token=TEST_TELEGRAM_BOT_TOKEN,
		)

		with self.assertRaises(ValidationError):
			TelegramBot.objects.create(
				name="Bot2",
				token=TEST_TELEGRAM_BOT_TOKEN,
			)


	def test_by_default_is_running_is_False(self):
		bot = TelegramBot.objects.create(
			name="Bot1",
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		bot_status = TelegramBotStatus.objects.get(bot=bot)
		self.assertFalse(bot_status.is_running)



class TelegramBotStatusModelTest(TestCase):


	def test_bot_status_updates_on_is_running_change(self):
		bot = TelegramBot.objects.create(
			name="Bot1",
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		bot.is_running = True
		bot.save()

		bot_status = TelegramBotStatus.objects.get(bot=bot)
		self.assertTrue(bot_status.is_running)


	def test_bot_status_is_updated_when_is_running_is_updated(self):
		bot = TelegramBot.objects.create(
			name="Bot1",
			token=TEST_TELEGRAM_BOT_TOKEN,
		)
		bot.is_running = True
		bot.save()
		bot_status = TelegramBotStatus.objects.get(bot=bot)

		time_1 = bot.updated_at
		time_2 = bot_status.updated_at

		self.assertAlmostEqual(time_1, time_2, delta=timedelta(seconds=1))
