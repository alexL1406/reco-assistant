from leds.apa102 import APA102
from architecture.service_structure import ServiceStructure
from leds.configuration.pattern_iterator import PatternIterable
from leds.configuration.patterns import Patterns
from interaction.recognition import RecognitionStates
from interaction.conversation import ConversationStates

import time
import threading
from gpiozero import LED


class Leds(ServiceStructure):

    PIXELS_N = 12

    def __init__(self, services_handle, leds_enabled=True):

        super().__init__(services_handle)
        self.name = "Leds"

        self.dev = APA102(num_led=self.PIXELS_N)
        self.leds_enabled = leds_enabled

        self.idle_iterator = PatternIterable(Patterns.DEFAULT_IDLE_PATTERN)
        self.detection_iterator = PatternIterable(Patterns.DETECTION_PATTERN)
        self.recording_iterator = PatternIterable(Patterns.RECORDING_PATTERN)
        self.processing_iterator = PatternIterable(Patterns.PROCESSING_PATTERN)
        self.answer_found_iterator = PatternIterable(Patterns.ANSWER_FOUND_PATTERN)
        self.answer_not_found_iterator = PatternIterable(Patterns.ANSWER_NOT_FOUND_PATTERN)

        self.iterator = self.idle_iterator

        self.power = LED(5)
        self.power.on()

        print("Start led thread")

        self.thread = threading.Thread(target=self.show_leds)
        self.thread.daemon = True
        self.thread.start()

    def show_leds(self):
        while True:
            if self.leds_enabled:
                pixels_list = next(self.iterator)

                for pixels in pixels_list:
                    self.dev.set_pixel(pixels[0], pixels[1], pixels[2], pixels[3])

                self.dev.show()

            time.sleep(0.2)
            self.show_leds()

    def set_mode(self, state):

        print("change leds mode: "+ str(state) )

        if state == RecognitionStates.IDLE:
            self.iterator = self.idle_iterator

        if state == RecognitionStates.SPEECH_DETECTION:
            self.iterator = self.detection_iterator

        if state == RecognitionStates.RECORDING:
            self.iterator = self.recording_iterator

        if state == RecognitionStates.PROCESSING:
            self.iterator = self.processing_iterator

        if state == ConversationStates.ANSWER_FOUND:
            self.iterator = self.answer_found_iterator

        if state == ConversationStates.ANSWER_NOT_FOUND:
            self.iterator = self.answer_not_found_iterator

    def set_enabled(self, enabled):

        self.leds_enabled = enabled
