import time
import pathlib
from architecture.service_structure import ServiceStructure

class Minuteur(ServiceStructure):

    def __init__(self, services_handle):

        super().__init__(services_handle)
        self.name = "Minuteur"
        self.duration = 0
        self.running = False
        self.file_directory = str(pathlib.Path.home()) + "/Reco-Assistant/reco-assistant/files/"
        self.alarm_file = None

        self.update_audio("rafiki-it-is-time.mp3")


    def update_duration(self, duration_in_sec):
        self.duration = duration_in_sec

    def update_audio(self, file_name):
        self.alarm_file = self.file_directory + file_name

    def start_minuteur(self):

        print("Start minuteur")
        self.running = True

        time.sleep(self.duration)

        self.services.audio_player.play_sound(self.alarm_file)
        self.running = False
