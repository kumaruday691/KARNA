from phue import Bridge
from time import sleep

from logging.ApplicationLogger import ApplicationLogger


class BridgeDecorator(object):

    # region Constructor

    def __init__(self, bridgeIp):
        self._component = None
        self._ipAddress = bridgeIp
        self.status = None

    # region Public Methods

    def initialize(self):
        try:
            self._component = Bridge(self._ipAddress)
            self._component.connect()
            return self
        except Exception as ex:
            ApplicationLogger().addError("Failed to initialize Hue bridge")
            return None

    def turnOnAll(self):
        self._toggleLights(True)

    def turnOffAll(self):
        self._toggleLights(False)

    def flicker(self):
        self._toggleLights(None)
        sleep(1)
        self._toggleLights(None)


    # region Helper Methods

    def _toggleLights(self, toggleState):
        lights = self._component.lights
        if not lights:
            return

        for light in lights:
            if toggleState is None:
                light.on = not light.on
                self.status = light.on
                return

            light.on = toggleState
            self.status = light.on

