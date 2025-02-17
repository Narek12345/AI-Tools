import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer



class TelegramBotStatusConsumer(AsyncWebsocketConsumer):


	async def connect(self):
		self.bot_id = self.scope['url_route']['kwargs']['bot_id']
		self.room_group_name = f"bot_status_{self.bot_id}"

		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		self.accept()


	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)


	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'status_message',
				'message': message,
			}
		)


	async def status_message(self, event):
		message = event['message']

		await self.send(text_data=json.dumps({
			'message': message
		}))
