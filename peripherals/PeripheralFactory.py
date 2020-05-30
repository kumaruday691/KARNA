from peripherals.hue.BridgeDecorator import BridgeDecorator
from peripherals.lcd import lcddriver


class PeripheralFactory(object):
    # region Constants

    HUE_ADDRESS = '192.168.86.174'

    # region Properties

    _instance = None
    _lcd = None
    _bridge = None

    # region Constructor

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PeripheralFactory, cls).__new__(cls)

        return cls._instance

    # region Public Methods

    def initialize(self):
        self._initializeLcd()
        self._initializeHueBridge()

    def getLcdDevice(self):
        return self._lcd

    def getHueBridge(self):
        return self._bridge

    # region Helper Methods

    def _initializeLcd(self):
        lcd = lcddriver.lcd()
        lcd.lcd_clear()
        self._lcd = lcd

    def _initializeHueBridge(self):
        bridgeDecorator = BridgeDecorator(self.HUE_ADDRESS)
        self._bridge = bridgeDecorator.initialize()
