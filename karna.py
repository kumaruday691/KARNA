from events.EventManager import EventManager
from peripherals.PeripheralFactory import PeripheralFactory


def initialize():
    PeripheralFactory().initialize()


def run():
    while True:
        _runEvents()


def _runEvents():
    eventManager = EventManager()
    eventManager.initialize()
    eventManager.run()


if __name__ == "__main__":
    initialize()
    run()
