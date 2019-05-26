from .expansion import Expansion
from game import *
import random

# TODO: figure out what is all needed to randomize with
kingdom_cards = ["Druid", "Faithful Hound", "Guardian", "Monastery", "Pixie", "Tracker", "Changeling", "Fool",
                 "Ghost Town", "Leprechaun", "Night Watchman", "Secret Cave", "Bard", "Blessed Village", "Cemetery",
                 "Conclave", "Devil's Workshop", "Exorcist", "Necromancer", "Shepherd", "Skulk", "Cobbler", "Crypt",
                 "Cursed Village", "Den of Sin", "Idol", "Pooka", "Sacred Grove", "Tormentor", "Tragic Hero", "Vampire",
                 "Werewolf", "Raider"]


class Nocturne(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = NOCTURNE
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        # TODO: add more card things
        self.presets = [
            dominion_presets,
            intrigue_presets,
            seaside_presets,
            alchemy_presets,
            prosperity_presets,
            cornucopia_presets,
            hinterlands_presets,
            dark_ages_presets,
            guilds_presets,
            adventures_presets,
            empires_presets,
            nocturne_presets,
            renaissance_presets
        ]

    @staticmethod
    def get_preset(other):
        return other.get_preset_(EXPANSIONS.index(NOCTURNE))

    # TODO: Implement draw (read rules)
    def draw(self):
        if self.number_of_cards == 0:
            return None
        return None
