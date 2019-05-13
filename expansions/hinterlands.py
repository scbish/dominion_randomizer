from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Crossroads", "Duchess", "Fool's Gold", "Develop", "Oasis", "Oracle", "Scheme", "Tunnel",
                 "Jack of all Trades", "Noble Brigand", "Nomad Camp", "Silk Road", "Spice Merchant", "Trader", "Cache",
                 "Cartographer", "Embassy", "Haggler", "Highway", "Ill-Gotten Gains", "Inn", "Mandarin", "Margrave",
                 "Stables", "Border Village", "Farmland"]

dominion_presets = [
    Game("Highway Robbery",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Highway", "Inn", "Margrave", "Noble Brigand", "Oasis"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Library", "Moneylender", "Throne Room", "Workshop"])]),
    Game("Adventures Abroad",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Fool's Gold", "Oracle", "Spice Merchant"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Laboratory", "Remodel", "Sentry", "Vassal"])]),
]

intrigue_presets = [
    Game("Money for Nothing",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Cartographer", "Jack of all Trades", "Silk Road", "Tunnel"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Replace", "Patrol", "Pawn", "Shanty Town", "Torturer"])]),
    Game("The Duke's Ball",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Duchess", "Haggler", "Inn", "Noble Brigand", "Scheme"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Duke", "Harem", "Masquerade", "Upgrade"])]),
]

seaside_presets = [
    Game("Travelers",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Crossroads", "Farmland", "Silk Road", "Stables"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Island", "Lookout", "Merchant Ship", "Warehouse"])]),
    Game("Diplomacy",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Embassy", "Farmland", "Ill-Gotten Gains", "Noble Brigand", "Trader"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Bazaar", "Caravan", "Embargo", "Smugglers"])]),
]

prosperity_presets = [
    Game("Instant Gratification",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Farmland", "Haggler", "Ill-Gotten Gains", "Noble Brigand", "Trader"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Expand", "Hoard", "Mint", "Watchtower"])]),
    Game("Treasure Trove",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Develop", "Fool's Gold", "Ill-Gotten Gains", "Mandarin"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Monument", "Royal Seal", "Trade Route", "Venture"])]),
]

hinterlands_presets = [
    Game("Introduction",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Crossroads", "Develop", "Haggler", "Jack of all Trades", "Margrave",
                                        "Nomad Camp", "Oasis", "Spice Merchant", "Stables"])]),
    Game("Fair Trades",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Cartographer", "Develop", "Duchess", "Farmland",
                                        "Ill-Gotten Gains", "Noble Brigand", "Silk Road", "Stables", "Trader"])]),
    Game("Bargains",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Cache", "Duchess", "Fool's Gold", "Haggler", "Highway",
                                        "Nomad Camp", "Scheme", "Spice Merchant", "Trader"])]),
    Game("Gambits",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Crossroads", "Embassy", "Inn", "Jack of all Trades",
                                        "Mandarin", "Nomad Camp", "Oasis", "Oracle", "Tunnel"])]),
]

dark_ages_presets = [
    Game("Far From Home",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Develop", "Embassy", "Fool's Gold", "Haggler"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Beggar", "Count", "Feodum", "Marauder", "Wandering Minstrel"],
                         extra_cards=["Ruins"])]),
    Game("Expeditions",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Highway", "Spice Merchant", "Tunnel"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Altar", "Catacombs", "Ironmonger", "Poor House", "Storeroom"])]),
]

empires_presets = [
    Game("Simple Plans",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Develop", "Haggler", "Ill-Gotten Gains", "Stables"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Catapult", "Forum", "Patrician", "Temple", "Villa"],
                         event_cards=["Donate"],
                         landmark_cards=["Labyrinth"])]),
    Game("Expansion",
         [ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Farmland", "Highway", "Spice Merchant", "Tunnel"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Charm", "Encampment", "Engineer", "Legionary"],
                         landmark_cards=["Battlefield", "Fountain"])]),
]


class Hinterlands(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = HINTERLANDS
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
        return other.get_preset_(EXPANSIONS.index(HINTERLANDS))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=HINTERLANDS,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
