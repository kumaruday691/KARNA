import datetime

from actions.DisplayAmbienceAction import DisplayAmbianceAction
from events.AbstractEvent import AbstractEvent


class TimeEvent(AbstractEvent):

    # region Constructor

    def __init__(self):
        super().__init__()
        pass

    # region Public Methods

    def initialize(self):
        self.actions.append(DisplayAmbianceAction())
        pass
