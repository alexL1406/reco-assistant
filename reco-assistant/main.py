# -*- coding: utf-8 -*-

from interaction.conversation import Conversation
from utils.audio_player import AudioPlayer

if __name__ == '__main__':

    audio_player = AudioPlayer()

    print("Init Conversation ")

    conversation = Conversation(audio_player)

    print("Start Conversation")

    conversation.start_interaction()
