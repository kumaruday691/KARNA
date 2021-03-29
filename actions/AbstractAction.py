from abc import abstractmethod, ABC


class AbstractAction(ABC):
    # region Constructor

    def __init__(self):
        super().__init__()
        pass

    # region Abstract Methods

    @abstractmethod
    def execute(self):
        pass
