from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_%s' % self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'resend',
                'el': text_data
            }
        )

    async def resend(self, event):
        print(event)
        el = event['el']
        await self.send(text_data=el)
