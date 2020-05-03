# -*- coding: utf-8 -*-

from interaction.recording import Recording
from utils.google_handle import GoogleHandle
import threading
import time

if __name__ == '__main__':

    recording = Recording()

    print("Run the recording")

    result = recording.start_recording()
