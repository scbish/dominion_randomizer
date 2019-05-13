from .constants import *


class Preset:
    def __init__(self, title=None,
                 first_expansion=None, second_expansion=None,
                 first_kingdom_cards=None, second_kingdom_cards=None,
                 first_treasure_cards=None, second_treasure_cards=None,
                 first_victory_cards=None, second_victory_cards=None,
                 first_starter_cards=None, second_starter_cards=None,
                 first_extra_cards=None, second_extra_cards=None,
                 first_event_cards=None, second_event_cards=None,
                 first_landmark_cards=None, second_landmark_cards=None):
        self.title = title
        self.first_expansion = PresetHalf(first_expansion,
                                          first_kingdom_cards,
                                          first_treasure_cards,
                                          first_victory_cards,
                                          first_starter_cards,
                                          first_extra_cards,
                                          first_event_cards,
                                          first_landmark_cards)
        self.second_expansion = PresetHalf(second_expansion,
                                           second_kingdom_cards,
                                           second_treasure_cards,
                                           second_victory_cards,
                                           second_starter_cards,
                                           second_extra_cards,
                                           second_event_cards,
                                           second_landmark_cards) if second_expansion else None

    def print(self):
        if self.second_expansion:
            print(self.first_expansion.name, "and", self.second_expansion.name, end=": ")
            print(self.title)
            print()
            self.first_expansion.print()
            self.second_expansion.print()
        else:
            print(self.first_expansion.name, "only", end=": ")
            print(self.title)
            print()
            self.first_expansion.print()


class PresetHalf:
    def __init__(self, name, kingdom_cards, treasure_cards, victory_cards, starter_cards, extra_cards, event_cards, landmark_cards):
        self.name = name
        self.kingdom_cards = kingdom_cards
        self.treasure_cards = treasure_cards
        self.victory_cards = victory_cards
        self.starter_cards = starter_cards
        self.extra_cards = extra_cards
        self.event_cards = event_cards
        self.landmark_cards = landmark_cards

    def print(self):
        if self.name:
            print(self.name)
        if self.kingdom_cards:
            print(KINGDOM + ":", self.kingdom_cards)
        if self.treasure_cards:
            print(TREASURE + ":", self.treasure_cards)
        if self.victory_cards:
            print(VICTORY + ":", self.victory_cards)
        if self.starter_cards:
            print(STARTER + ":", self.starter_cards)
        if self.extra_cards:
            print(EXTRA + ":", self.extra_cards)
        if self.event_cards:
            print(EVENT + ":", self.event_cards)
        if self.landmark_cards:
            print(LANDMARK + ":", self.landmark_cards)
        if self.name:
            print()
