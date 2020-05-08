import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
import pathlib

class Minuteur(object):

    def __init__(self, duration_in_sec):
        self.duration = duration_in_sec
        self.running = False
        self.file_directory = str(pathlib.Path.home()) + "/Reco-Assistant/reco-assistant/files/"
        self.audio = None

        self.update_audio("rafiki-it-is-time.mp3")


    def update_duration(self, duration_in_sec):
        self.duration = duration_in_sec

    def update_audio(self, file_name):
        alarm_file = self.file_directory + file_name
        self.audio = AudioSegment.from_file(alarm_file)

    def start_minuteur(self):

        print("Start minuteur")
        self.running = True

        time.sleep(self.duration)

        play(self.audio)
        self.running = False
