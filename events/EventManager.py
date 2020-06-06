from events.ProximityEvent import ProximityEvent
from events.TimeEvent import TimeEvent


class EventManager(object):

    # region Constructor

    def __init__(self):
        self.events = []

    # region Public Methods

    def initialize(self):
        self.events.append(TimeEvent())
        self.events.append(ProximityEvent())

    def run(self):
        for event in self.events:
            event.run()
