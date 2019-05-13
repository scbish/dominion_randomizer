from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Embargo", "Haven", "Lighthouse", "Native Village", "Pearl Diver", "Ambassador", "Fishing Village",
                 "Lookout", "Smugglers", "Warehouse", "Caravan", "Cutpurse", "Island", "Navigator", "Pirate Ship",
                 "Salvager", "Sea Hag", "Treasure Map", "Bazaar", "Explorer", "Ghost Ship", "Merchant Ship", "Outpost",
                 "Tactician", "Treasury", "Wharf"]

dominion_presets = [
    Game("Reach for Tomorrow",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Ghost Ship", "Lookout", "Sea Hag", "Treasure Map"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Cellar", "Council Room", "Vassal", "Village"])]),
    Game("Repetition",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Explorer", "Outpost", "Pearl Diver", "Pirate Ship", "Treasury"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Harbinger", "Militia", "Workshop", "Caravan"])]),
    Game("Give and Take",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Haven", "Island", "Salvager", "Smugglers"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Library", "Market", "Moneylender", "Witch", "Ambassador"])]),
]

intrigue_presets = [
    Game("A Star to Steer By",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Lookout", "Treasure Map", "Ghost Ship", "Haven", "Outpost"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Secret Passage", "Diplomat", "Swindler", "Wishing Well", "Courtier"])]),
    Game("Shore Patrol",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Island", "Wharf", "Cutpurse", "Lighthouse", "Warehouse"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Patrol", "Replace", "Shanty Town", "Trading Post", "Pawn"])]),
    Game("Bridge Crossing",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Salvager", "Embargo", "Smugglers", "Native Village", "Treasury"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Lurker", "Nobles", "Duke", "Conspirator", "Bridge"])]),
]

seaside_presets = [
    Game("High Seas",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Bazaar", "Caravan", "Embargo", "Explorer", "Haven", "Island", "Lookout",
                                        "Pirate Ship", "Smugglers", "Wharf"])]),
    Game("Buried Treasure",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Cutpurse", "Fishing Village", "Lighthouse", "Outpost",
                                        "Pearl Diver", "Tactician", "Treasure Map", "Warehouse", "Wharf"])]),
    Game("Shipwrecks",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ghost Ship", "Merchant Ship", "Native Village", "Navigator", "Pearl Diver",
                                        "Salvager", "Sea Hag", "Smugglers", "Treasury", "Warehouse"])]),
]

prosperity_presets = [
    Game("Exploding Kingdom",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Lookout", "Outpost", "Tactician", "Wharf"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "City", "Grand Market", "King's Court", "Quarry"])]),
    Game("Pirate Bay",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Bazaar", "Lighthouse", "Pirate Ship", "Smugglers", "Warehouse"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Expand", "Hoard", "Mint", "Trade Route", "Watchtower"])]),
]

hinterlands_presets = [
    Game("Travelers",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Island", "Lookout", "Merchant Ship", "Warehouse"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Crossroads", "Farmland", "Silk Road", "Stables"])]),
    Game("Diplomacy",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Bazaar", "Caravan", "Embargo", "Smugglers"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Embassy", "Farmland", "Ill-Gotten Gains", "Noble Brigand", "Trader"])]),
]

dark_ages_presets = [
    Game("Watery Graves",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Native Village", "Pirate Ship", "Salvager", "Treasure Map", "Treasury"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Count", "Graverobber", "Hermit", "Scavenger", "Urchin"])]),
    Game("Treasury Peasants",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Haven", "Island", "Lookout", "Warehouse"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Death Cart", "Feodum", "Poor House", "Urchin", "Vagrant"],
                         extra_cards=["Ruins"])]),
]

empires_presets = [
    Game("Boxed In",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Salvager", "Smugglers", "Tactician", "Warehouse", "Wharf"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Chariot Race", "Encampment", "Enchantress", "Gladiator"],
                         event_cards=["Tax"],
                         landmark_cards=["Wall"])]),
    Game("King of the Sea",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Explorer", "Haven", "Native Village", "Pirate Ship", "Sea Hag"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Farmers' Market", "Overlord", "Temple", "Wild Hunt"],
                         event_cards=["Delve"],
                         landmark_cards=["Fountain"])]),
]


class Seaside(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = SEASIDE
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
        return other.get_preset_(EXPANSIONS.index(SEASIDE))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=SEASIDE,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
