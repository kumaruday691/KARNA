import ephem
import datetime

from appLogging.ApplicationLogger import ApplicationLogger
from common import Utility


class AstralDecorator(object):

    # region Constructor

    def __init__(self):
        self._location = self._initializeLocation()

    # region Public Methods

    def getNextSunriseAndSunset(self):
        if self._location is None:
            return None, None

        sun = ephem.Sun()
        riseTimeEphem = self._location.next_rising(sun)
        setTimeEphem = self._location.next_setting(sun)
        return self._convertEphemTimeToLocalTime(riseTimeEphem), self._convertEphemTimeToLocalTime(setTimeEphem)

    def getNextMoonrise(self):
        if self._location is None:
            return None

        moon = ephem.Moon()
        riseTimeEphem = self._location.next_rising(moon)
        return self._convertEphemTimeToLocalTime(riseTimeEphem)

    def getNextFullMoon(self):
        dateNowString = datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M")
        fullMoonEphem = ephem.next_full_moon(dateNowString)
        return self._convertEphemTimeToLocalTime(fullMoonEphem)

    def getNextEquinox(self):
        dateNowString = datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M")
        equinioxEphem = ephem.next_equinox(dateNowString)
        return self._convertEphemTimeToLocalTime(equinioxEphem)

    def getNextSolstice(self):
        dateNowString = datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M")
        solsticeEphem = ephem.next_equinox(dateNowString)
        return self._convertEphemTimeToLocalTime(solsticeEphem)

    # region Helper Methods

    def _initializeLocation(self):
        try:
            location = ephem.Observer()
            lat, lng = Utility.getHomeLocation()
            location.lat = lat
            location.lon = lng
            return location
        except Exception as ex:
            ApplicationLogger().addError("failed to fetch astral location")
            return None

    def _convertEphemTimeToLocalTime(self, ephemTime):
        ephemTimeTuple = ephemTime.tuple()
        if not ephemTimeTuple or len(ephemTimeTuple) < 6:
            return None

        year, month, day, hour, minute = ephemTimeTuple[0], ephemTimeTuple[1], ephemTimeTuple[2], ephemTimeTuple[3], ephemTimeTuple[4]
        constructedDate = datetime.datetime(year, month, day, hour, minute, second=0)
        constructedString = constructedDate.strftime("%Y/%m/%d %H:%M")
        ephemDate = ephem.Date(constructedString)
        return ephem.localtime(ephemDate)