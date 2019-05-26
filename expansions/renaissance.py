from .expansion import Expansion
from game import *
import random

# TODO: figure out what is all needed to randomize with
kingdom_cards = ["Border Guard", "Ducat", "Lackeys", "Acting Troupe", "Cargo Ship", "Experiment", "Improve",
                 "Flag Bearer", "Hideout", "Inventor", "Mountain Village", "Patron", "Priest", "Research",
                 "Silk Merchant", "Old Witch", "Recruiter", "Scepter", "Scholar", "Sculptor", "Seer", "Spices",
                 "Swashbuckler", "Treasurer", "Villain"]

dark_ages_presets = []


class Renaissance(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = RENAISSANCE
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
        return other.get_preset_(EXPANSIONS.index(RENAISSANCE))

    # TODO: Implement draw (read rules)
    def draw(self):
        if self.number_of_cards == 0:
            return None
        return None
