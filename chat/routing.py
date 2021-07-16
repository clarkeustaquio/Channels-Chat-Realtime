from django.urls import path
from .consumers import ChatConsumer

ws_chat_urlpatterns = [
    path('ws/chat-consumer/', ChatConsumer.as_asgi())
]