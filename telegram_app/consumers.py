import json
import asyncio

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from telegram_app.models import TelegramBot, TelegramBotStatus



class TelegramBotStatusConsumer(AsyncWebsocketConsumer):


	async def connect(self):
		self.bot_id = self.scope['url_route']['kwargs']['bot_id']
		self.room_group_name = f"bot_status_{self.bot_id}"

		await self.channel_layer.group_add(
			self.room_group_name, self.channel_name
		)

		await self.accept()


	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name, self.channel_name
		)
		await self.close()


	@sync_to_async
	def get_bot(self, bot_id):
		try:
			return TelegramBot.objects.get(id=bot_id)
		except TelegramBot.DoesNotExist:
			return None


	@sync_to_async
	def change_bot_status(self, bot, bot_status):
		new_bot_status = TelegramBotStatus.objects.get(bot=bot)
		new_bot_status.is_running = bot_status
		new_bot_status.save()


	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		to_status = text_data_json['to_status']
		bot_id = text_data_json['bot_id']

		bot = await self.get_bot(bot_id)

		if not bot:
			status_message = f"Бот с ID {bot_id} не найден."
			await self.send(text_data=json.dumps({
				'status': status_message
			}))
			return

		if to_status == "start":
			docker_command = f"docker run -d --name bot_{bot.id} -e TELEGRAM_BOT_TOKEN={bot.token} telegram_bot"
			try:
				process = await asyncio.create_subprocess_shell(
					docker_command,
					stdout=asyncio.subprocess.PIPE,
					stderr=asyncio.subprocess.PIPE
				)
				stdout, stderr = await process.communicate()

				if process.returncode == 0:
					status_message = "Бот успешно запущен!"
					await self.change_bot_status(bot, True)
				else:
					status_message = f"Ошибка при запуске Docker контейнера: {stderr.decode()}"
			except Exception as e:
				status_message = f"Ошибка при выполнении команды Docker: {str(e)}"
		else:
			status_message = "Другой статус."

		# Отправляем результат в WebSocket.
		await self.send(text_data=json.dumps({
			'status': status_message
		}))
