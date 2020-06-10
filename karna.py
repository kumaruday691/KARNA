from appLogging.ApplicationLogger import ApplicationLogger
from common.AstralDecorator import AstralDecorator
from events.EventManager import EventManager
from peripherals.PeripheralFactory import PeripheralFactory
from peripherals.speaker.SpeechAdapter import SpeechAdapter
from schedule.EventScheduler import EventScheduler


def initialize():
    PeripheralFactory().initialize()
    SpeechAdapter.checkForErrors("All sensors are functional.")


def run():
    while True:
        _runEvents()


def _runEvents():
    eventManager = EventManager()
    eventManager.initialize()
    eventManager.run()


if __name__ == "__main__":
    try:
        initialize()
        run()
        # sc = EventScheduler()
        # sc.initialize()
        # while True:
        #     pass
    except Exception as ex:
        print(ApplicationLogger().getErrors())
        print("Exception caught")
