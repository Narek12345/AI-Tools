from django.shortcuts import render
from django.http import HttpResponse

from telegram_app.forms import ConnectTelegramBotForm


def home_telegram_page(request):
	return render(request, 'telegram_app/home_telegram.html')


def connect_bot(request):
	if request.method == 'POST':
		form = ConnectTelegramBotForm(data=request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ConnectTelegramBotForm()

	context = {'form': form}
	return render(request, 'telegram_app/connect_bot.html', context)
