import threading
# import flask
# from twilio.twiml.messaging_response import MessagingResponse

from appLogging.ApplicationLogger import ApplicationLogger
from events.EventManager import EventManager
from peripherals.PeripheralFactory import PeripheralFactory
from peripherals.speaker.SpeechAdapter import SpeechAdapter
from schedule.EventScheduler import EventScheduler

# app = flask.Flask(__name__)
#
#
# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     from_number = flask.request.form['From']
#     to_number = flask.request.form['To']
#     body = flask.request.form['Body']
#
#     print(from_number, to_number, body)
#     resp = MessagingResponse()
#
#     resp.message("The Robots are coming! Head for the hills!")
#
#     return str(resp)
#

def initialize():
    PeripheralFactory().initialize()
    SpeechAdapter.checkForErrors("All sensors are functional.")
    threading.Thread(target=EventScheduler().initialize).start()


def run():
    # threading.Thread(target=app.run).start()
    while True:
        _runEvents()


def _runEvents():
    eventManager = EventManager()
    eventManager.initialize()
    eventManager.run()


if __name__ == "__main__":
    try:
        initialize()
        run()
    except Exception as ex:
        print(ApplicationLogger().getErrors())
        print("Exception caught")
