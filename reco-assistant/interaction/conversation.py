from architecture.service_structure import ServiceStructure
from interaction.chatbots.minuteur_chatbot import MinuteurChatBot
from interaction.recognition import RecognitionStates

import base64
import time
import threading


class ConversationStates:
    ANSWER_FOUND = "Answer found"
    ANSWER_NOT_FOUND = "Answer not found"

class Conversation(ServiceStructure):

    def __init__(self, services_handle):
        super().__init__(services_handle)
        self.name = "Conversation"

        self.configuration_json = None
        self.chatbots_list = []
        self.keyword_list = []

        self.set_configuration()

    def set_configuration(self):
        self.chatbots_list = [MinuteurChatBot(self.services, find_number=True)]
        self.keyword_list = [chatbot.keyword for chatbot in self.chatbots_list]

    def switch_conversation_state(self, state):
        print("switch recording state")
        self.services.leds.set_mode(state)
        time.sleep(2)
        self.services.recognition.switch_recognition_state(RecognitionStates.IDLE)

    def switch_conversation_state_thread(self, state):
        threading.Thread(target=lambda: self.switch_conversation_state(state)).start()

    def start_interaction(self):

        recognition_dict = self.services.recognition.start_recognition()

        if recognition_dict["success"]:

            result, language, confidence = recognition_dict["results"]

            print(self.keyword_list)

            answer = ""

            for index, keyword in enumerate(self.keyword_list):
                if keyword+ " " in result:
                    print("start chatbot with keyword {}".format(keyword))
                    chatbot = self.chatbots_list[index]
                    answer = self.chatbots_list[index].get_answer(result, language)

            if answer:
                self.switch_conversation_state_thread(ConversationStates.ANSWER_FOUND)
                print(answer)
                answer_wav = base64.b64decode(self.services.google_handle.text_to_speech_api(answer, language).encode('ascii'))
                self.services.audio_player.play_from_wav_content(answer_wav)

            else:
                self.switch_conversation_state_thread(ConversationStates.ANSWER_NOT_FOUND)
                time.sleep(2)

        else:
            self.switch_conversation_state_thread(ConversationStates.ANSWER_NOT_FOUND)
