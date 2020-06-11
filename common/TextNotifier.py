from twilio.rest import Client
import os

from appLogging.ApplicationLogger import ApplicationLogger


class TextNotifier(object):

    # region Constructor

    def __init__(self):
        self._client = self._initializeClient()

    # region Public Methods

    def send(self, message):
        if self._client is None:
            return

        try:
            myNumber = os.getenv('myNum')
            fromNumber = os.getenv('fromNum')
            self._client.messages.create(to=myNumber, body=message, from_=fromNumber)
        except Exception as ex:
            print(ex)
            ApplicationLogger().addError("Failed to send text")

    # region Helper Methods

    def _initializeClient(self):
        try:
            sid = os.environ['TWILIO_SID']
            auth = os.environ['TWILIO_AUTH']
            return Client(sid, auth)
        except Exception as ex:
            print(ex)
            ApplicationLogger().addError("Failed to initialize twilio")
