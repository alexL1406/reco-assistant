# -*- coding: utf-8 -*-

from interaction.conversation import Conversation
from utils.google_handle import GoogleHandle
import threading
import time

if __name__ == '__main__':

    print("Init Conversation ")

    conversation = Conversation()

    print("Start Conversation")

    conversation.start_interaction()
