import json
import dateparser

from common import Utility


class TileTracker(object):

    # region Constructor

    def __init__(self):
        pass

    # region Public Methods

    def isHome(self):
        tileJson = self._readTileJson()
        if tileJson is None:
            return None

        phoneId = tileJson['f5d960b9c337cb1d']['last_tile_state']
        if phoneId is None:
            return None

        timstamp = phoneId['timestamp']
        lat = phoneId['latitude']
        lng = phoneId['longitude']

        knownDate = dateparser.parse(str(timstamp))
        hlat, hlng = Utility.getHomeLocation()
        homeLat = float(hlat)
        homeLng = float(hlng)

        return round(lat, 2) == round(homeLat, 2) and round(lng, 2) == round(homeLng, 2), knownDate

    # region Helper Methods

    def _readTileJson(self):
        try:
            with open('../tileJson.js', 'r') as fr:
                text = fr.read().replace("\'", "\"").replace("None", "\"None\"").replace("True", "\"True\"").replace("False", "\"False\"")
                jsonText = json.loads(text)
                return jsonText
        except Exception as ex:
            print(ex)
            return None


