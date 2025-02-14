from django import forms

from telegram_app.models import TelegramBot



class ConnectTelegramBotForm(forms.ModelForm):
	"""Форма для добавления нового Telegram бота."""

	class Meta:
		model = TelegramBot
		fields = ('name', 'token')
		widgets = {
			'name': forms.fields.TextInput(
				attrs={
					'placeholder': 'Введите название бота',
				}
			),
			'token': forms.fields.TextInput(
				attrs={
					'placeholder': 'Вставьте токен вашего бота',
				}
			)
		}
		error_messages = {
			'name': {'required': 'Поле должно быть заполнено'},
			'token': {'required': 'Поле должно быть заполнено'},
		}
