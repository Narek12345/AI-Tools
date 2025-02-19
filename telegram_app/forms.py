from django import forms

from telegram_app.models import TelegramBot



class ConnectTelegramBotForm(forms.ModelForm):
    """Форма для добавления нового Telegram бота."""

    class Meta:
        model = TelegramBot
        fields = ('name', 'token')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название бота',
                    'class': 'form-control'
                }
            ),
            'token': forms.TextInput(
                attrs={
                    'placeholder': 'Вставьте токен вашего бота',
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'name': 'Название бота',
            'token': 'Токен бота'
        }
        error_messages = {
            'name': {'required': 'Поле должно быть заполнено'},
            'token': {'required': 'Поле должно быть заполнено'},
        }
