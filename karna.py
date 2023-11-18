import threading
import flask
from twilio.twiml.messaging_response import MessagingResponse

from appLogging.ApplicationLogger import ApplicationLogger
from events.EventManager import EventManager
from peripherals.PeripheralFactory import PeripheralFactory
from peripherals.speaker.SpeechAdapter import SpeechAdapter
from schedule.EventScheduler import EventScheduler


def initialize():
    PeripheralFactory().initialize()
    SpeechAdapter.checkForErrors("All sensors are functional.")
    threading.Thread(target=EventScheduler().initialize).start()


def run():
    while True:
        _runEvents()


def _runEvents():
    eventManager = EventManager()
    eventManager.initialize()
    threading.Thread(target=eventManager.run).start()


if __name__ == "__main__":
    try:
        initialize()
        run()
    except Exception as ex:
        print(ApplicationLogger().getErrors())
        print("Exception caught")
