from datetime import datetime

from appLogging.ApplicationLogger import ApplicationLogger


class SchedulerManager(object):

    # region Properties

    _instance = None
    _events = {}

    # region Constructor

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SchedulerManager, cls).__new__(cls)

        return cls._instance

    # region Public Methods

    def addEvent(self, scheduler, action):
        if len(action) < 3:
            return

        actionName = action[0]
        actionTime = action[1]
        actionEvent = action[2]

        nowTimestamp = datetime.now().timestamp()
        if nowTimestamp > actionTime:
            return

        if actionName not in self._events.keys():
            self._events[actionName] = actionEvent
            scheduler.enterabs(actionTime, 1, actionEvent)

    def cancelEvent(self, name, scheduler):
        if name not in self._events.keys():
            return

        try:
            event = self._events[name]
            scheduler.cancel(event)
        except Exception as ex:
            ApplicationLogger().addError("Failed to remove event")

    def removeEvent(self, name):
        if name not in self._events.keys():
            return

        del self._events[name]
