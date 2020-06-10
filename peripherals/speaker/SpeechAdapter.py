from gtts import gTTS
import os

from appLogging.ApplicationLogger import ApplicationLogger
from common.constants import DEF_LANG, DEF_AUDIO_PATH


class SpeechAdapter(object):

    # region Public Methods

    @staticmethod
    def checkForErrors(successMessage):
        errors = ApplicationLogger().getErrors()
        if len(errors) == 0:
            SpeechAdapter.playNow(successMessage)
            return

        for error in errors:
            SpeechAdapter.playNow(error)

        ApplicationLogger().clearErrors()

    @staticmethod
    def playNow(text):
        SpeechAdapter.save(text)
        SpeechAdapter.play()

    @staticmethod
    def save(speechText):
        try:
            speechObj = gTTS(text=speechText, lang=DEF_LANG, slow=False)
            speechObj.save(DEF_AUDIO_PATH)
            return True
        except Exception as ex:
            ApplicationLogger().addError("Unable to save audio file")
            return False

    @staticmethod
    def play():
        try:
            os.system("omxplayer {0} > /dev/null".format(DEF_AUDIO_PATH))
            os.remove(DEF_AUDIO_PATH)
        except Exception as ex:
            ApplicationLogger().addError("Unable to remove audio file")

