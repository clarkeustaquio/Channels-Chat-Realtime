from django.urls import path
from .consumers import APIConsumer

ws_urlpatterns = [
    path('ws/random-int/', APIConsumer.as_asgi())
]