import threading
from picamera import PiCamera
from time import sleep

from appLogging.ApplicationLogger import ApplicationLogger


class CameraAdapter(object):

    # region Constructor

    def __init__(self):
        pass

    # region Public Methods

    def snap(self):
        threading.Thread(target=self._snap).start()

    def record(self):
        threading.Thread(target=self._record).start()

    def iterativeSnap(self, iterations=5):
        threading.Thread(target=self._iterativeSnap, args=[iterations]).start()

    # region Helper Methods

    def _snap(self):
        try:
            cam = PiCamera()
            cam.capture('/home/pi/karna/snaps/tmp_img.jpg')
        except Exception as ex:
            ApplicationLogger().addError('taking snap failed.')

    def _record(self):
        try:
            cam = PiCamera()
            cam.start_recording('/home/pi/karna/records/record.h264')
            sleep(30)
            cam.stop_recording()
        except Exception as ex:
            print(ex)
            ApplicationLogger().addError("Failed to record video")

    def _iterativeSnap(self, iterations=5):
        try:
            cam = PiCamera()
            for i in range(iterations):
                sleep(5)
                cam.capture('/home/pi/karna/snaps/snap%s.jpg' % i)
        except Exception as ex:
            ApplicationLogger().addError('failed to take snaps.')


if __name__ == '__main__':
    adapter = CameraAdapter()
    adapter.record()