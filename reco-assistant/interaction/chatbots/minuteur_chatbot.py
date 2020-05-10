from interaction.chatbots.chat_bot_structure import ChatBotStucture
from interaction.chatbots.identifier import Identifier, IdentifierType
from utils.minuteur import Minuteur
import time



class MinuteurChatBot(ChatBotStucture):

    def __init__(self, minuteur, find_number=False):

        super().__init__(find_number)

        self.minuteur = minuteur

        self.keyword = "minuteur"

        identifier_time_unity = Identifier("time unity", IdentifierType.CONTEXT)
        identifier_time_unity.add_content_from_list(["secondes", "seconde", "minute", "minutes", "heure", "heures"])

        self.identifiers_list = [identifier_time_unity]

    def get_answer(self, recognition_result, language):
        super().get_answer(recognition_result, language)

        print("get_answer minuteur")

        list_time_unity = self.speech_dict["time unity"]
        list_duration = self.speech_dict["numbers"]

        if len(list_time_unity) and len(list_duration):

            converter = 1

            if "second" in list_time_unity[0]:
                converter = 1
            elif "minute" in list_time_unity[0]:
                converter = 60
            elif "heure" in list_time_unity[0]:
                converter = 3600

            print("duration {} * {}".format(list_duration[0], converter))
            self.minuteur.update_duration(list_duration[0]*converter)

            self.run_behavior(lambda: self.minuteur.start_minuteur())

            return "Je lance un minuteur de {} {}".format(list_duration[0], list_time_unity[0])



