from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from django.shortcuts import render, HttpResponse
from .models import Chat

channel_layer = get_channel_layer()

def lobby(request):
    chats = Chat.objects.all().order_by('id')

    return render(request, 'chat/lobby.html', {
        'chats': chats,
    })