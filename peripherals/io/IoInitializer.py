import RPi.GPIO as GPIO

from common.constants import PROX_1_PIN, TAIL_LAMP_OUT_PIN


class IoInitializer(object):

    # region Constructor

    def __init__(self):
        pass

    # region Public Methods

    def initialize(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self._initializeInputs()
        self._initializeOutputs()

    # region Helper Methods

    def _initializeInputs(self):
        GPIO.setup(PROX_1_PIN, GPIO.IN)

    def _initializeOutputs(self):
        GPIO.setup(TAIL_LAMP_OUT_PIN, GPIO.OUT)