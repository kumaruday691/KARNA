import Adafruit_DHT

from logging.ApplicationLogger import ApplicationLogger


class HumiditySensor(object):

    # region Constants

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

    # region Constructor

    def __init__(self):
        pass

    # region Public Methods

    def readVitals(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
            return humidity, temperature
        except Exception as ex:
            ApplicationLogger().addError("Failed to initialize humidity sensor")

