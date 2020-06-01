from phue import Bridge
from time import sleep

from appLogging.ApplicationLogger import ApplicationLogger


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

        for i in range(len(lights)):
            if toggleState is None:
                self._component.lights[i].on = not self._component.lights[i].on
                continue

            self._component.lights[i].on = toggleState
            self.status = self._component.lights[i].on

