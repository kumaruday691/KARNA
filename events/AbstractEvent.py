from abc import ABC, abstractmethod


class AbstractEvent(ABC):

    # region Constructor

    def __init__(self):
        super().__init__()
        self.actions = []
        self.initialize()

    # region Abstract Methods

    @abstractmethod
    def initialize(self):
        pass

    # region Shared Methods

    def run(self):
        for action in self.actions:
            action.execute()
