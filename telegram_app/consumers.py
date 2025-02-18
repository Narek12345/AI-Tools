import json
import asyncio

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from telegram_app.models import TelegramBot



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


	@sync_to_async
	def get_bot(self, bot_id):
		try:
			return TelegramBot.objects.get(id=bot_id)
		except TelegramBot.DoesNotExist:
			return None


	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		to_status = text_data_json['to_status']
		bot_id = text_data_json['bot_id']

		print(f"Received command for bot {bot_id} with status {to_status}")

		bot = await self.get_bot(bot_id)

		if not bot:
			status_message = f"Бот с ID {bot_id} не найден."
			print(status_message)
			await self.send(text_data=json.dumps({
				'status': status_message
			}))
			return

		if to_status == "start":
			docker_command = f"docker run -d --name bot_{bot.id} -e TELEGRAM_BOT_TOKEN={bot.token} telegram_bot"
			try:
				# Запуск команды docker асинхронно
				process = await asyncio.create_subprocess_shell(
					docker_command,
					stdout=asyncio.subprocess.PIPE,
					stderr=asyncio.subprocess.PIPE
				)
				stdout, stderr = await process.communicate()

				if process.returncode == 0:
					status_message = "Бот успешно запущен!"
					print("Docker container started successfully!")
				else:
					status_message = f"Ошибка при запуске Docker контейнера: {stderr.decode()}"
					print(f"Error: {stderr.decode()}")
			except Exception as e:
				status_message = f"Ошибка при выполнении команды Docker: {str(e)}"
				print(f"Exception: {str(e)}")
		else:
			status_message = "Другой статус."
			print(status_message)

		# Отправляем результат в WebSocket
		await self.send(text_data=json.dumps({
			'status': status_message
		}))
