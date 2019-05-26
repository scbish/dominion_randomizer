from expansions.constants import *


class Game:
    def __init__(self, title, expansion_cards):
        self.title = title
        self.expansion_cards = expansion_cards

    def print(self):
        if len(self.expansion_cards) == 1:
            print(self.expansion_cards[0].name, "only", end=": ")
            print(self.title)
            print()
            self.expansion_cards[0].print()
        else:
            print(", ".join(expansion_card.name for expansion_card in self.expansion_cards), end=": ")
            print(self.title)
            print()
            for expansion_card in self.expansion_cards:
                expansion_card.print()


class ExpansionCards:
    def __init__(self,
                 name=None,
                 kingdom_cards=None,
                 treasure_cards=None,
                 victory_cards=None,
                 bane_cards=None,
                 starter_cards=None,
                 extra_cards=None,
                 event_cards=None,
                 landmark_cards=None):
        self.name = name
        self.kingdom_cards = kingdom_cards
        self.treasure_cards = treasure_cards
        self.victory_cards = victory_cards
        self.bane_cards = bane_cards
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
        if self.bane_cards:
            print(BANE + ":", self.bane_cards)
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
