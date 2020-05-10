from interaction.recognition import Recognition
from interaction.chatbots.minuteur_chatbot import MinuteurChatBot
from utils.minuteur import Minuteur
from utils.google_handle import GoogleHandle

class Conversation(object):

    def __init__(self, audio_player):
        self.audio_player = audio_player
        self.recognition = Recognition()
        self.configuration_json = None
        self.chatbots_list = []
        self.keyword_list = []

        self.minuteur = Minuteur(self.audio_player)

        self.set_configuration()

    def set_configuration(self):
        self.chatbots_list = [MinuteurChatBot(self.minuteur, find_number=True)]
        self.keyword_list = [chatbot.keyword for chatbot in self.chatbots_list]

    def start_interaction(self):

        result, confidence, language = self.recognition.start_recording()

        print(self.keyword_list)

        for index, keyword in enumerate(self.keyword_list):
            if keyword+ " " in result:
                print("start chatbot with keyword {}".format(keyword))
                chatbot = self.chatbots_list[index]
                answer = self.chatbots_list[index].get_answer(result, language)

                print(answer)










