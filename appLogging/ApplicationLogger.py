class ApplicationLogger(object):
    # region Properties

    _instance = None
    _errors = []
    _warnings = []

    # region Constructor

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ApplicationLogger, cls).__new__(cls)

        return cls._instance

    # region Public Methods

    def addError(self, error):
        self._errors.append(error)

    def addWarning(self, warning):
        self._warnings.append(warning)
