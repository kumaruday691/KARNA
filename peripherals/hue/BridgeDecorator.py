from phue import Bridge

from logging.ApplicationLogger import ApplicationLogger


class BridgeDecorator(object):

    # region Constructor

    def __init__(self, bridgeIp):
        self._component = None
        self._ipAddress = bridgeIp

    # region Public Methods

    def initialize(self):
        try:
            self._component = Bridge(self._ipAddress)
            self._component.connect()
            return self._component
        except Exception as ex:
            ApplicationLogger().addError("Failed to initialize Hue bridge")
            return None
