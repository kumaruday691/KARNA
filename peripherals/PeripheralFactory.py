from common.constants import START_UP_START
from peripherals.hue.BridgeDecorator import BridgeDecorator
from peripherals.io.IoInitializer import IoInitializer
from peripherals.lcd import lcddriver
from peripherals.speaker.SpeechAdapter import SpeechAdapter


class PeripheralFactory(object):
    # region Constants

    HUE_ADDRESS = '192.168.1.74'

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
        self._initializeSpeech()
        self._initializeLcd()
        self._initializeHueBridge()
        self._initializeIo()

    def getLcdDevice(self):
        return self._lcd

    def getHueBridge(self):
        return self._bridge

    # region Helper Methods

    def _initializeSpeech(self):
        SpeechAdapter.playNow(START_UP_START)

    def _initializeIo(self):
        IoInitializer().initialize()

    def _initializeLcd(self):
        lcd = lcddriver.lcd()
        lcd.lcd_clear()
        self._lcd = lcd
        self._lcd.lcd_display_string("Initializing...", 1)

    def _initializeHueBridge(self):
        bridgeDecorator = BridgeDecorator(self.HUE_ADDRESS)
        self._bridge = bridgeDecorator.initialize()
        if self._bridge:
            self._lcd.lcd_display_string("Hue Bridge Connected", 2)
            self._bridge.flicker()
        else:
            self._lcd.lcd_display_string("Hue Bridge Unavailable", 2)

