import os


def getEnvironmentVariable(key, defaultValue):
    try:
        acquiredValue = os.environ.get(key)
        if acquiredValue is None:
            return defaultValue

        return acquiredValue
    except Exception:
        return defaultValue


def getHomeLocation():
    lat = getEnvironmentVariable('homeLat', '31.4589713')
    lng = getEnvironmentVariable('homeLng', '-101.4403715')
    return lat, lng