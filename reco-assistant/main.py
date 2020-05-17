# -*- coding: utf-8 -*-
from architecture.services_handle import ServicesHandle
from interaction.conversation import Conversation
from utils.audio_player import AudioPlayer
from utils.google_handle import GoogleHandle

if __name__ == '__main__':

    services_handle = ServicesHandle()

    print("Init Services ")
    services_handle.start_services()

    while True:
        input("Pres ENTER to start the recognition")
        services_handle.conversation.start_interaction()
