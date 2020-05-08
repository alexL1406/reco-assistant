

class IdentifierType:
    NUMBER = "Number"
    CONTEXT = "Context"


class Identifier(object):

    def __init__(self, name,  identifier_type):
        self.name = name
        self.type = identifier_type
        self.content_list = []

    def add_content(self, word):

        self.content_list.append(word)

    def add_content_from_list(self, list):

        self.content_list =self.content_list + list






