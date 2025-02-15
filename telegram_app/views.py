from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from telegram_app.models import TelegramBot
from telegram_app.forms import ConnectTelegramBotForm


def home_telegram_page(request):
	return render(request, 'telegram_app/home_telegram.html')


def connect_bot(request):
	if request.method == 'POST':
		form = ConnectTelegramBotForm(data=request.POST)
		if form.is_valid():
			bot = form.save()
			return redirect('telegram_app:show_bot', bot_id=bot.id)
	else:
		form = ConnectTelegramBotForm()

	context = {'form': form}
	return render(request, 'telegram_app/connect_bot.html', context)


def show_bot(request, bot_id):
	bot = get_object_or_404(TelegramBot, id=bot_id)

	context = {'bot': bot}
	return render(request, 'telegram_app/bot_page.html', context)


def start_bot(request, bot_id):
	"""Запускает Telegram bot."""
	bot = get_object_or_404(TelegramBot, id=bot_id)
	bot.is_running = True
	bot.save()

	messages.success(request, "Бот запущен")
	return redirect('telegram_app:show_bot', bot_id=bot_id)
