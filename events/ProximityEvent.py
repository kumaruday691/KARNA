from actions.TailLampAction import TailLampAction
from events.AbstractEvent import AbstractEvent


class ProximityEvent(AbstractEvent):

    # region Constructor

    def __init__(self):
        super().__init__()
        pass

    # region Public Methods

    def initialize(self):
        self.actions.append(TailLampAction())