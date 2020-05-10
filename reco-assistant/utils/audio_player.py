import os
from subprocess import run, Popen, PIPE
from threading import Thread



class AudioPlayer(object):

    def __init__(self):
        thread = Thread(target=self.start_jack_server())
        thread.start()
        print("thread started")


    def play_sound(self, file):

        run(["mpg123", file])
        print("sound played")

    def start_jack_server(self):

        print("Start jack server")
        process = Popen(["jackd", "-d", "alsa"], stdout=PIPE)

        print("end of jack server")
