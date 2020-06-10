from abc import ABC, abstractmethod


class AbstractSchedule(ABC):

    # region Constructor

    def __init__(self):
        super().__init__()
        self._callbacks = []

    # region Shared Methods

    def addCallback(self, name, time, callbackFn):
        self._callbacks.append((name, time, callbackFn))

    def getCallbacks(self):
        return self._callbacks

    # region Abstract Methods

    @abstractmethod
    def schedule(self):
        pass