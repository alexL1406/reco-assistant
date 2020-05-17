# -*- coding: utf-8 -*-
from architecture.service_structure import ServiceStructure

import audioop
import pyaudio
import wave
import threading
import pathlib
import base64


class RecognitionStates:
    SPEECH_DETECTION = "Speech Detection"
    RECORDING = "Recording"
    PROCESSING = "Processing"
    IDLE = "IDLE"


class Recognition(ServiceStructure):

    def __init__(self, services_handle):
        super().__init__(services_handle)
        self.name = "Recognition"

        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 4
        self.sample_frequency = 44100  # Record at 44100 samples per second
        self.recognition_state = RecognitionStates.IDLE
        self.stream = None
        self.pyAudio_interface = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.filename = str(pathlib.Path.home()) + "/.local/share/speech.wav"
        self.audio_fragment_array = []  # Initialize array to store frames

        self.DELTA_RECORDING = 0.3
        self.initial_audio_length = int(self.DELTA_RECORDING * self.sample_frequency / self.chunk)
        self.previous_rms = 0

        self.RMS_THRESHOlD_UP = 2
        self.RMS_THRESHOlD_DOWN = -0.6

        # self.recording_thread = threading.Thread(target=self.start_recording())
        self.detect_bos_thread = None
        self.detect_eos_thread = None
        self.write_to_files_thread = None

        self.google_handle = self.services.google_handle
        self.audio_player = self.services.audio_player

    def __del__(self):

        # Terminate the PortAudio interface
        self.pyAudio_interface.terminate()

    def start_recognition(self):
        print("Initialize Audio Stream")
        self.stream = self.pyAudio_interface.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.sample_frequency,
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


        audio_bytes = self.stop_recording()

        self.write_to_files_thread = threading.Thread(target=lambda: self.services.audio_player.write_to_file_from_bytes(
            audio_bytes, self.channels, self.filename))
        self.write_to_files_thread.start()

        return self.get_recognition_result()

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

        # Stop and close the stream
        self.stream.stop_stream()
        self.stream.close()

        return b''.join(self.audio_fragment_array)

    def write_to_file(self, audio_bytes):
        print('Writing in file')
        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.pyAudio_interface.get_sample_size(self.sample_format))
        wf.setframerate(self.sample_frequency)
        wf.writeframes(audio_bytes)
        wf.close()

    def get_recognition_result(self):

        print("Convert bytes to 1 channel")
        audio_bytes_4channels = b''.join(self.audio_fragment_array)
        audio_bytes_2channels = audioop.tomono(audio_bytes_4channels, 2, 0.5, 0.5)
        audio_bytes_1channel = audioop.tomono(audio_bytes_2channels, 2, 0.5, 0.5)

        print("Start speech interaction request to google")
        request_json = self.services.google_handle.speech_to_text_api(base64.b64encode(audio_bytes_1channel)
                                                               ,self.sample_frequency)

        dict_output = {"success": False, "results": ()}

        if request_json:
            print(request_json)
            dict_output["success"] = True
            recognition_result = str(request_json['results'][0]['alternatives'][0]['transcript'])
            confidence_result = float(request_json['results'][0]['alternatives'][0]['confidence'])
            language_result = request_json['results'][0]['languageCode']

            print("Request succeed, result: {}, confidence: {}".format(recognition_result, confidence_result))

            dict_output["results"] = (recognition_result, language_result, confidence_result)

        return dict_output
