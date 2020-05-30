from events.TimeEvent import TimeEvent


class EventManager(object):

    # region Constructor

    def __init__(self):
        self.events = []

    # region Public Methods

    def initialize(self):
        self.events.append(TimeEvent())

    def run(self):
        for event in self.events:
            event.run()
