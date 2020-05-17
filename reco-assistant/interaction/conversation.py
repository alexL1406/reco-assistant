from architecture.service_structure import ServiceStructure
from interaction.chatbots.minuteur_chatbot import MinuteurChatBot

import base64


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
                print(answer)
                answer_wav = base64.b64decode(self.services.google_handle.text_to_speech_api(answer, language).encode('ascii'))
                self.services.audio_player.play_from_wav_content(answer_wav)

