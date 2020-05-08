import time
from text_to_num import text2num
from interaction.chatbots.identifier import IdentifierType
from threading import Thread



class ChatBotStucture(object):

    def __init__(self):

        self.keyword = ""
        self.identifiers_list = []
        self.speech_dict = {}
        self.behavior_thread = None
        self.behavior_started = False

    def get_speech_dict(self, recognition_result, language):
        print("Start get_speech_dict")
        speech_list = recognition_result.split()

        self.speech_dict.update({"keyword": self.keyword})
        speech_list.remove(self.keyword)

        for identifier in self.identifiers_list:
            words_by_identifier = []
            if identifier.type == IdentifierType.NUMBER:

                for word in speech_list:

                    number = None
                    try:
                        number = text2num(word, language[0:2])

                    except ValueError:
                        try:
                            number = int(word)
                        except ValueError:
                            pass
                    finally:
                        if number:
                            words_by_identifier.append(number)
                            speech_list.remove(word)

            elif identifier.type == IdentifierType.CONTEXT:
                words_by_identifier = list(set(speech_list) & set(identifier.content_list))
                for word in words_by_identifier:
                    speech_list.remove(word)

            self.speech_dict.update({identifier.name: words_by_identifier})

        self.speech_dict.update({"other": speech_list})
        print("Speech dictionary {}".format(self.speech_dict))

    def get_answer(self, recognition_result, language):
        print("Start get_answer")
        self.get_speech_dict(recognition_result, language)

    def run_behavior(self, method):
        self.behavior_started = True
        self.behavior_thread = Thread(target=method)
        self.behavior_thread.start()




