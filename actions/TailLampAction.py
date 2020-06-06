import RPi.GPIO as GPIO

from actions.AbstractAction import AbstractAction
from common.constants import PROX_1_PIN, TAIL_LAMP_OUT_PIN


class TailLampAction(AbstractAction):

    # region Constructor

    def __init__(self):
        super().__init__()
        pass

    # region Public Methods

    def execute(self):
        if GPIO.input(PROX_1_PIN):
            GPIO.output(TAIL_LAMP_OUT_PIN, GPIO.LOW)
        else:
            GPIO.output(TAIL_LAMP_OUT_PIN, GPIO.HIGH)


