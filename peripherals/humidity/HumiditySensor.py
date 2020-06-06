import Adafruit_DHT

from appLogging.ApplicationLogger import ApplicationLogger
from common.constants import DHT_PIN


class HumiditySensor(object):

    # region Constants

    DHT_SENSOR = Adafruit_DHT.DHT11

    # region Constructor

    def __init__(self):
        pass

    # region Public Methods

    def readVitals(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, DHT_PIN)
            return humidity, temperature
        except Exception as ex:
            ApplicationLogger().addError("Failed to initialize humidity sensor")

