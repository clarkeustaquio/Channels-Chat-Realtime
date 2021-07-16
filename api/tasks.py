from celery import shared_task
from core.celery import app

from asyncio import sleep
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from random import randint

channel_layer = get_channel_layer()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'api.tasks.add',
        'schedule': 1.0,
        # 'args': (16, 16)
    },
}

@shared_task
def add():
   words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

   async_to_sync(channel_layer.group_send)('room', {'type': 'send_word', 'message': words[randint(0, len(words) - 1)]})

   return True