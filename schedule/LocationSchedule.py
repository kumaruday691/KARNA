import os
from datetime import datetime
from appLogging.ApplicationLogger import ApplicationLogger
from schedule.AbstractSchedule import AbstractSchedule
from schedule.SchedulerManager import SchedulerManager


class LocationSchedule(AbstractSchedule):

    # region Constructor

    def __init__(self):
        super(LocationSchedule, self).__init__()
        self._nextScheduleTime = None


    # region Public Methods

    def schedule(self):
        scheduleTime = None
        if self._nextScheduleTime is None:
            scheduleTime = datetime.now().timestamp() + 10
        else:
            scheduleTime = self._nextScheduleTime

        self.addCallback("location", scheduleTime, self.gatherLocationAction)
        self._nextScheduleTime = scheduleTime + (20 * 60)

    # region Actions

    def gatherLocationAction(self):
        try:
            os.system('python3 /home/pi/tile.py')
            os.system('js-beautify tileJson.txt > tileJson.js')
            SchedulerManager().removeEvent('location')
        except Exception as ex:
            SchedulerManager().removeEvent('location')
            ApplicationLogger().addError("failed to gather location")
