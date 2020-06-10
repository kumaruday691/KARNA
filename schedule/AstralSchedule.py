from common.AstralDecorator import AstralDecorator
from peripherals.speaker.SpeechAdapter import SpeechAdapter
from schedule.AbstractSchedule import AbstractSchedule
from datetime import datetime
import playsound

from schedule.SchedulerManager import SchedulerManager


class AstralSchedule(AbstractSchedule):

    # region Constructor

    def __init__(self):
        super(AstralSchedule, self).__init__()
        self._astral = AstralDecorator()
        pass

    # region Abstract Methods

    def schedule(self):
        self._scheduleSunriseAndSunset()
        self._scheduleMoonrise()

    # region Actions

    def sunriseAction(self):
        print("sunrise")
        SchedulerManager().removeEvent('sunrise')
        pass

    def sunsetAction(self):
        SpeechAdapter().playNow('Sun is about to set in 30 minutes.')
        SchedulerManager().removeEvent('sunset')
        pass

    def moonriseAction(self):
        print("moonrise")
        SchedulerManager().removeEvent('moonrise')
        pass

    # region Helper Methods

    def _scheduleSunriseAndSunset(self):
        sunriseTime, sunsetTime = self._astral.getNextSunriseAndSunset()
        self.addCallback("sunrise", sunriseTime.timestamp(), self.sunriseAction)
        self.addCallback("sunset", sunsetTime.timestamp() - 30 * 60, self.sunsetAction)

    def _scheduleMoonrise(self):
        moonriseTime = self._astral.getNextMoonrise()
        self.addCallback('moonrise', moonriseTime.timestamp(), self.moonriseAction)
