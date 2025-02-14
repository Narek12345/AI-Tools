from django.test import TestCase

from telegram_app.models import TelegramBot
from telegram_app.forms import ConnectTelegramBotForm



class ConnectTelegramBotFormTest(TestCase):
	"""Тест формы для добавления Telegram бота."""


	def test_form_telegram_bot_input_has_placeholder_and_css_classes(self):
		"""Тест: форма отображает текстовое поле ввода."""
		form = ConnectTelegramBotForm()
		self.assertIn("placeholder='Введите название бота'", form.as_p())
		self.assertIn("placeholder='Вставьте токен вашего бота'", form.as_p())


	def test_form_validation_for_blank_fields(self):
		"""Тест: проверка валидации для пустых полей."""
		form = ConnectTelegramBotForm(data={'telegram_bot_name': '', 'telegram_bot_token': ''})
		self.assertFalse(form.is_valid())


	def test_form_save(self):
		"""Тест сохранения формы."""
		form = ConnectTelegramBotForm(
			data={
				'telegram_bot_name': 'Telegram bot',
				'telegram_bot_token': '8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg'
			}
		)
		self.assertTrue(form.is_valid())
		new_telegram_bot = form.save()
		self.assertEqual(new_telegram_bot, TelegramBot.objects.first())
