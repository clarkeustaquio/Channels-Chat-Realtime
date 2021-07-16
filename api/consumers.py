import json
# from time import sleep
from asyncio import sleep
from random import randint
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class APIConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print(self.scope)
        await self.channel_layer.group_add('room', self.channel_name)
        await self.accept()


    async def disconnect(self):
        await self.channel_layer.group_discard('room', self.channel_name)

    async def send_word(self, event):
        event_word = event['message']
        await self.send(text_data=event_word)

    # async def connect(self):
    #     await self.accept()   

    #     for x in range(10):
    #         await self.send(json.dumps({'message': randint(0, 1000)}))
    #         await sleep(1)

    # def receive(self, text_data, bytes_data):
    #     self.send(text_data="Test!")
        