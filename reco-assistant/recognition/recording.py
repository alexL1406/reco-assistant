# -*- coding: utf-8 -*-

import audioop
import pyaudio
import wave
import threading
import pathlib


class RecognitionStates:

    SPEECH_DETECTION = "Speech Detection"
    RECORDING = "Recording"
    PROCESSING = "Processing"
    IDLE = "IDLE"


class Recording(object):

    def __init__(self):
        super().__init__()
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 4
        self.fs = 44100  # Record at 44100 samples per second
        self.recognition_state = RecognitionStates.IDLE
        self.stream = None
        self.pyAudio_interface = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.filename = str(pathlib.Path.home())+"/.local/share/speech.wav"
        self.audio_fragment_array = []  # Initialize array to store frames

        self.DELTA_RECORDING = 0.2
        self.initial_audio_length = int(self.DELTA_RECORDING * self.fs / self.chunk)
        self.previous_rms = 0

        self.RMS_THRESHOlD_UP = 2
        self.RMS_THRESHOlD_DOWN = -0.6
        self.recording_thread = threading.Thread(target=self.start_recording())
        self.detect_bos_thread = None
        self.detect_eos_thread = None

    def start_recording(self):
        print("Initialize Audio Stream")
        self.stream = self.pyAudio_interface.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.fs,
            frames_per_buffer=self.chunk,
            input=True)

        print("Calculate initial RMS")

        initial_fragment = self.record_fragment()

        self.previous_rms = audioop.rms(initial_fragment, self.channels)

        print("Initial RMS {}".format(self.previous_rms))

        print("Start recording")
        self.switch_recording_state(RecognitionStates.SPEECH_DETECTION)

        while (self.recognition_state == RecognitionStates.SPEECH_DETECTION
               or self.recognition_state == RecognitionStates.RECORDING):
            fragment = self.record_fragment()
            self.audio_fragment_array.append(fragment)

            if self.recognition_state == RecognitionStates.SPEECH_DETECTION:
                self.detect_bos_thread = threading.Thread(target=lambda: self.detect_bos(fragment))
                self.detect_bos_thread.start()

                if len(self.audio_fragment_array) > 2:
                    del self.audio_fragment_array[0]

            if self.recognition_state == RecognitionStates.RECORDING:
                self.detect_eos_thread = threading.Thread(target=lambda: self.detect_eos(fragment))
                self.detect_eos_thread.start()

        self.stop_recording()

    def start_recording_thread(self):
        self.recording_thread.start()

    def switch_recording_state(self, state):
        self.recognition_state = state
        print("Recording state: {}".format(state))

    def detect_bos(self, fragment):
        rms_rate = self.calculate_rms_rate(fragment)

        if rms_rate > self.RMS_THRESHOlD_UP:
            self.switch_recording_state(RecognitionStates.RECORDING)

    def detect_eos(self, fragment):
        rms_rate = self.calculate_rms_rate(fragment)

        if rms_rate < self.RMS_THRESHOlD_DOWN:
            self.switch_recording_state(RecognitionStates.PROCESSING)

    def calculate_rms_rate(self, fragment):
        rms = audioop.rms(fragment, self.channels)
        rate = (rms - self.previous_rms) / self.previous_rms
        print("% RMS: {}", rate)
        self.previous_rms = rms
        return rate

    def record_fragment(self):
        initial_audio_frames_array = []
        for i in range(int(self.initial_audio_length)):
            data = self.stream.read(self.chunk)
            initial_audio_frames_array.append(data)

        return b''.join(initial_audio_frames_array)

    def stop_recording(self):
        print('Finished recording')
        self.switch_recording_state(RecognitionStates.IDLE)

        # Stop and close the stream
        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        self.pyAudio_interface.terminate()

        print('Writing in file')
        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.pyAudio_interface.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.audio_fragment_array))
        wf.close()
