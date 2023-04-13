from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.http import JsonResponse

from heyoo import WhatsApp
from twilio.rest import Client

import os
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework import status
# Create your views here.
class Index(APIView):
    permission_classes=''
    def get(self, request, *args, **kwargs):
        return Response({'msg': 'this is the first page'},status=200)
    


class WhatsAppView(APIView):
    permission_classes =''
    def post(self, request):
        # Get the uploaded file and message text from the request data
        # file = request.FILES.get('file')
        # message = request.data.get('message')
        message="hello just for try"

        # Get the list of phone numbers from the request data
        # phone_numbers = request.data.get('phone_numbers')
        phone_numbers=['916394939653']

        # Your Twilio account SID and auth token
        account_sid = 'AC4b76af4ae655c5cca4f3a50f4db50e56'
        auth_token = '1ed064238495dbd2a0b29dc75a1e1cc0'

        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Loop through the list of phone numbers and send a WhatsApp message with attachment to each one
        message_sids = []
        for phone_number in phone_numbers:
            message = client.messages.create(
                from_='whatsapp:+14155238886', # Twilio sandbox number
                to=f'whatsapp:+{phone_number}', # User's WhatsApp number
                body=message,
                # media_url=file.url # URL of the uploaded file
            )
            message_sids.append(message.sid)

        return Response({'status': 'success', 'message_sids': message_sids})



#send whatsnumber by facebook developer account.
class WhatsAppSms(APIView):
    messenger = WhatsApp('EABJj1xxxxxx',phone_number_id='1130xxxxxxxx')
    # For sending a Text messages
    messenger.send_message('Hello I am WhatsApp Cloud API', '91989155xxxx')
    # For sending an Image
    messenger.send_image(
        image="https://i.imgur.com/YSJayCb.jpeg",
        recipient_id="91989155xxxx",
    )