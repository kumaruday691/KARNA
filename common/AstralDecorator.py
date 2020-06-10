import ephem
import datetime


class AstralDecorator(object):

    # region Constants

    LOC_LAT = "31.4638"
    LOC_LONG = "-100.4370"

    # region Constructor

    def __init__(self):
        self._location = self._initializeLocation()

    # region Public Methods

    def getNextSunriseAndSunset(self):
        sun = ephem.Sun()
        riseTimeEphem = self._location.next_rising(sun)
        setTimeEphem = self._location.next_setting(sun)
        return self._convertEphemTimeToLocalTime(riseTimeEphem), self._convertEphemTimeToLocalTime(setTimeEphem)

    def getNextMoonrise(self):
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
        location = ephem.Observer()
        location.lat = self.LOC_LAT
        location.lon = self.LOC_LONG
        return location

    def _convertEphemTimeToLocalTime(self, ephemTime):
        ephemTimeTuple = ephemTime.tuple()
        if not ephemTimeTuple or len(ephemTimeTuple) < 6:
            return None

        year, month, day, hour, minute = ephemTimeTuple[0], ephemTimeTuple[1], ephemTimeTuple[2], ephemTimeTuple[3], ephemTimeTuple[4]
        constructedDate = datetime.datetime(year, month, day, hour, minute, second=0)
        constructedString = constructedDate.strftime("%Y/%m/%d %H:%M")
        ephemDate = ephem.Date(constructedString)
        return ephem.localtime(ephemDate)