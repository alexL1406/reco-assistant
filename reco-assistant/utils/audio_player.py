import os
from subprocess import run, Popen, PIPE
from threading import Thread
import wave
import pathlib



class AudioPlayer(object):

    def __init__(self):
        self.sample_frequency = 44100
        self.sample_width = 2
        thread = Thread(target=self.start_jack_server())
        thread.start()
        print("thread started")


    def play_sound(self, file):

        run(["mpg123", file])
        print("sound played")

    def play_wav(self, file):

        run(["aplay", file])
        print("wav played")

    def start_jack_server(self):

        print("Start jack server")
        process = Popen(["jackd", "-d", "alsa"], stdout=PIPE)

        print("end of jack server")

    def write_to_file_from_bytes(self, audio_bytes, path, channels):

        print('Writing in file')
        # Save the recorded data as a WAV file
        wf = wave.open(path, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(self.sample_width)
        wf.setframerate(self.sample_frequency)
        wf.writeframes(audio_bytes)
        wf.close()

    def write_to_file_from_wav(self, wav_content, path):
        with open(path, 'wb') as file:
            file.write(wav_content)

    def play_from_wav_content(self, wav_string):

        path = str(pathlib.Path.home()) + "/.local/share/answer.wav"
        self.write_to_file_from_wav(wav_string, path)
        self.play_wav(path)

