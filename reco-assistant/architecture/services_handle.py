from enum import Enum
from interaction import conversation, recognition
from utils import audio_player, google_handle, minuteur


class ServicesHandle(object):

    def __init__(self):

        self.conversation = None
        self.recognition = None
        self.audio_player = None
        self.google_handle = None
        self.minuteur = None

    def start_services(self):

        print("start services")
        self.conversation = conversation.Conversation(self)
        self.recognition = recognition.Recognition(self)
        self.audio_player = audio_player.AudioPlayer(self)
        self.google_handle = google_handle.GoogleHandle(self)
        self.minuteur = minuteur.Minuteur(self)

        print("services started")
