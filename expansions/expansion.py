from abc import ABC
import random


class Expansion(ABC):
    @staticmethod
    def get_preset(other):
        pass

    def get_preset_(self, index):
        return random.choice(self.presets[index])
