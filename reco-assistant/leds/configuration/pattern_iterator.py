import time


class PatternIterable:
    def __iter__(self):
        return self

    def __init__(self, pattern_dict_list):

        self.pattern_list = [[[key] + pattern_dict[key] for key in pattern_dict.keys()] for pattern_dict in pattern_dict_list]
        self.index = 0

    def __next__(self):
        if self.index >= len(self.pattern_list):
            self.index = 0

        pixels_list = self.pattern_list[self.index]
        self.index += 1
        return pixels_list
