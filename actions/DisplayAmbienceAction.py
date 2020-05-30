import datetime
import math

from actions.AbstractAction import AbstractAction
from peripherals.PeripheralFactory import PeripheralFactory
from peripherals.humidity.HumiditySensor import HumiditySensor


class DisplayAmbianceAction(AbstractAction):

    # region Constructor

    def __init__(self):
        super().__init__()
        self.lcd = PeripheralFactory().getLcdDevice()

    # region Abstract Methods

    def execute(self):
        # guard clause - no lcd
        if not self.lcd:
            return

        now = datetime.datetime.now()
        humidity, temperature = HumiditySensor().readVitals()
        if humidity is not None and temperature is not None:
            atmDisplay = "Hum:{0}% Tmp:{1}*C".format(math.floor(humidity), math.floor(temperature))
            self.lcd.lcd_display_string(now.strftime("%a %d %I:%M:%S"), 1)
            self.lcd.lcd_display_string(atmDisplay, 2)
