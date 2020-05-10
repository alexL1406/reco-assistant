import time
import os
import pathlib

class Minuteur(object):

    def __init__(self, audio_player):
        self.audio_player = audio_player
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

        self.audio_player.play_sound(self.alarm_file)
        self.running = False
