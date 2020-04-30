# -*- coding: utf-8 -*-

from recognition.recording import Recording
import threading
import time

if __name__ == '__main__':

    recording = Recording()

    print("Run the recording")

    recording.start_recording()
