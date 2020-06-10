import sched, time, datetime

from schedule.AstralSchedule import AstralSchedule
from schedule.SchedulerManager import SchedulerManager


class EventScheduler(object):

    # region Constructor

    def __init__(self):
        self.schedules = []
        self._component = sched.scheduler(time.time, time.sleep)
        self._mainEvent = None
        self._currentScheduleTime = None
        self._nextScheduleTime = None

    # region Public Methods

    def initialize(self):
        currentTimeExtended = datetime.datetime.now().timestamp() + 5
        self.schedules.append(AstralSchedule())
        self._mainEvent = self._component.enterabs(currentTimeExtended, 1, self.scheduleEvents)
        self._component.run()
        pass

    def scheduleEvents(self):
        print("executed")
        for schedule in self.schedules:
            schedule.schedule()
            actions = schedule.getCallbacks()
            for action in actions:
                SchedulerManager().addEvent(self._component, action)

        currentTimeExtended = datetime.datetime.now().timestamp() + 60
        self._mainEvent = self._component.enterabs(currentTimeExtended, 1, self.scheduleEvents)
        pass

    def runAction(self):
        print("Run action")
        pass