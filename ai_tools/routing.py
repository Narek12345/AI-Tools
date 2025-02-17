from django.urls import re_path
from telegram_app import consumers

websocket_urlpatterns = [
    re_path(r'ws/telegram_bot/status/(?P<bot_id>\d+)/$', consumers.TelegramBotStatusConsumer.as_asgi()),
]
