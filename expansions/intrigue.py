from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Courtyard", "Lurker", "Pawn", "Masquerade", "Shanty Town", "Steward", "Swindler", "Wishing Well",
                 "Baron", "Bridge", "Conspirator", "Diplomat", "Ironworks", "Mill", "Mining Village", "Secret Passage",
                 "Courtier", "Duke", "Minion", "Patrol", "Replace", "Torturer", "Trading Post", "Upgrade", "Harem",
                 "Nobles"]

dominion_presets = [
    Game("Underlings",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Courtier", "Diplomat", "Minion", "Nobles", "Pawn"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Library", "Sentry", "Vassal"])]),
    Game("Grand Scheme",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Mill", "Mining Village", "Patrol", "Shanty Town"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Council Room", "Market", "Militia", "Workshop"])]),
    Game("Deconstruction",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Diplomat", "Harem", "Lurker", "Replace", "Swindler"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Mine", "Remodel", "Throne Room", "Village"])]),
]

intrigue_presets = [
    Game("Victory Dance",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Courtier", "Duke", "Harem", "Ironworks", "Masquerade", "Mill",
                                        "Nobles", "Patrol", "Replace"])]),
    Game("The Plot Thickens",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Ironworks", "Lurker", "Pawn", "Mining Village",
                                        "Secret Passage", "Steward", "Swindler", "Torturer", "Trading Post"])]),
    Game("Best Wishes",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Conspirator", "Courtyard", "Diplomat", "Duke", "Secret Passage",
                                        "Shanty Town", "Torturer", "Upgrade", "Wishing Well"])]),
]

seaside_presets = [
    Game("A Star to Steer By",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Secret Passage", "Diplomat", "Swindler", "Wishing Well", "Courtier"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Lookout", "Treasure Map", "Ghost Ship", "Haven", "Outpost"])]),
    Game("Shore Patrol",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Patrol", "Replace", "Shanty Town", "Trading Post", "Pawn"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Island", "Wharf", "Cutpurse", "Lighthouse", "Warehouse"])]),
    Game("Bridge Crossing",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Lurker", "Nobles", "Duke", "Conspirator", "Bridge"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Salvager", "Embargo", "Smugglers", "Native Village", "Treasury"])]),
]

prosperity_presets = [
    Game("Paths to Victory",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Harem", "Pawn", "Shanty Town", "Upgrade"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Counting House", "Goons", "Monument", "Peddler"])]),
    Game("All Along the Watchtower",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Mill", "Mining Village", "Pawn", "Torturer"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Hoard", "Talisman", "Trade Route", "Vault", "Watchtower"])]),
    Game("Lucky Seven",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Lurker", "Patrol", "Swindler", "Wishing Well"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Expand", "Forge", "King's Court", "Vault"])]),
]

hinterlands_presets = [
    Game("Money for Nothing",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Replace", "Patrol", "Pawn", "Shanty Town", "Torturer"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Cartographer", "Jack of all Trades", "Silk Road", "Tunnel"])]),
    Game("The Duke's Ball",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Duke", "Harem", "Masquerade", "Upgrade"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Duchess", "Haggler", "Inn", "Noble Brigand", "Scheme"])]),
]

dark_ages_presets = [
    Game("Prophecy",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Conspirator", "Nobles", "Secret Passage", "Wishing Well"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Armory", "Ironmonger", "Mystic", "Rebuild", "Vagrant"])]),
    Game("Invasion",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Diplomat", "Harem", "Swindler", "Torturer", "Upgrade"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Beggar", "Marauder", "Rogue", "Squire", "Urchin"],
                         extra_cards=["Ruins"])]),
]

empires_presets = [
    Game("Delicious Torture",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Bridge", "Harem", "Ironworks", "Torturer"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Crown", "Enchantress", "Sacrifice", "Settlers"],
                         event_cards=["Banquet"],
                         landmark_cards=["Arena"])]),
    Game("Buddy System",
         [ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Masquerade", "Mining Village", "Nobles", "Pawn", "Trading Post"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Capital", "Catapult", "Engineer", "Forum"],
                         event_cards=["Salt the Earth"],
                         landmark_cards=["Wolfden"])]),
]


class Intrigue(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = INTRIGUE
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        self.presets = [
            dominion_presets,
            intrigue_presets,
            seaside_presets,
            prosperity_presets,
            hinterlands_presets,
            dark_ages_presets,
            empires_presets,
        ]

    @staticmethod
    def get_preset(other):
        return other.get_preset_(EXPANSIONS.index(INTRIGUE))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=INTRIGUE,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
