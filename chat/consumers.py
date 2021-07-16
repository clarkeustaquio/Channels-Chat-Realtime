import json
from .models import Chat
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('lobby', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('lobby', self.channel_name)
        return await super().disconnect(code)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat = text_data_json['message']

        await self.channel_layer.group_send('lobby', {
            'type': 'send_chat',
            'chat': chat
        })

        await self.post_chat(chat)

    async def send_chat(self, event):
        message = event['chat']
        await self.send(text_data=message)

    @database_sync_to_async
    def post_chat(self, chat):
        Chat.objects.create(chat=chat)