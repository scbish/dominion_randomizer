from .expansion import Expansion
from game import *
import random
from numpy.random import hypergeometric

kingdom_cards = ["Engineer", "City Quarter", "Overlord", "Royal Blacksmith", "Encampment/Plunder", "Patrician/Emporium",
                 "Settlers/Bustling Village", "Castles", "Catapult/Rocks", "Chariot Race", "Enchantress",
                 "Farmers' Market", "Gladiator/Fortune", "Sacrifice", "Temple", "Villa", "Archive", "Capital", "Charm",
                 "Crown", "Forum", "Groundskeeper", "Legionary", "Wild Hunt"]
event_cards = ["Triumph", "Annex", "Donate", "Advance", "Delve", "Tax", "Banquet", "Ritual", "Salt the Earth",
               "Wedding", "Windfall", "Conquest", "Dominate"]
landmark_cards = ["Aqueduct", "Arena", "Bandit Fort", "Basilica", "Baths", "Battlefield", "Colonnade", "Defiled Shrine",
                  "Fountain", "Keep", "Labyrinth", "Mountain Pass", "Museum", "Obelisk", "Orchard", "Palace", "Tomb",
                  "Tower", "Triumphal Arch", "Wall", "Wolf Den"]

dominion_presets = [
    Game("Everything in Moderation",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Enchantress", "Forum", "Legionary", "Overlord", "Temple"],
                         event_cards=["Windfall"],
                         landmark_cards=["Orchard"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Library", "Remodel", "Village", "Workshop"])]),
    Game("Silver Bullets",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Catapult", "Charm", "Farmers' Market", "Groundskeeper", "Patrician"],
                         event_cards=["Conquest"],
                         landmark_cards=["Aqueduct"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Gardens", "Laboratory", "Market", "Moneylender"])]),
]

intrigue_presets = [
    Game("Delicious Torture",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Crown", "Enchantress", "Sacrifice", "Settlers"],
                         event_cards=["Banquet"],
                         landmark_cards=["Arena"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Bridge", "Harem", "Ironworks", "Torturer"])]),
    Game("Buddy System",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Capital", "Catapult", "Engineer", "Forum"],
                         event_cards=["Salt the Earth"],
                         landmark_cards=["Wolfden"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Masquerade", "Mining Village", "Nobles", "Pawn", "Trading Post"])]),
]

seaside_presets = [
    Game("Boxed In",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Chariot Race", "Encampment", "Enchantress", "Gladiator"],
                         event_cards=["Tax"],
                         landmark_cards=["wall"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Salvager", "Smugglers", "Tactician", "Warehouse", "Wharf"])]),
    Game("King of the Sea",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Farmers' Market", "Overlord", "Temple", "Wild Hunt"],
                         event_cards=["Delve"],
                         landmark_cards=["Fountain"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Explorer", "Haven", "Native Village", "Pirate Ship", "Sea Hag"])]),
]

prosperity_presets = [
    Game("Big Time",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Capital", "Gladiator", "Patrician", "Royal Blacksmith", "Villa"],
                         event_cards=["Dominate"],
                         landmark_cards=["Obelisk"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Forge", "Grand Market", "Loan", "Royal Seal"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
    Game("Gilded Gates",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Chariot Race", "City Quarter", "Encampment", "Groundskeeper", "Wild Hunt"],
                         landmark_cards=["Basilica", "Palace"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Monument", "Mint", "Peddler", "Talisman"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
]

hinterlands_presets = [
    Game("Simple Plans",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Catapult", "Forum", "Patrician", "Temple", "Villa"],
                         event_cards=["Donate"],
                         landmark_cards=["Labyrinth"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Develop", "Haggler", "Ill-Gotten Gains", "Stables"])]),
    Game("Expansion",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Charm", "Encampment", "Engineer", "Legionary"],
                         landmark_cards=["Battlefield", "Fountain"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Farmland", "Highway", "Spice Merchant", "Tunnel"])]),
]

dark_ages_presets = [
    Game("Tomb of the Rat King",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Chariot Race", "City Quarter", "Legionary", "Sacrifice"],
                         event_cards=["Advance"],
                         landmark_cards=["Tomb"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Death Cart", "Fortress", "Pillage", "Rats", "Storeroom"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"])]),
    Game("Triumph of the Bandit King",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Capital", "Charm", "Engineer", "Groundskeeper", "Legionary"],
                         event_cards=["Triumph"],
                         landmark_cards=["Defiled Shrine"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Catacombs", "Hunting Grounds", "Market Square", "Procession"],
                         starter_cards=["Shelters"])]),
    Game("The Squire's Ritual",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Catapult", "Crown", "Patrician", "Settlers"],
                         event_cards=["Ritual"],
                         landmark_cards=["Museum"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Feodum", "Hermit", "Ironmonger", "Rogue", "Squire"],
                         starter_cards=["Shelters"])]),
]

empires_presets = [
    Game("Basic Intro",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Chariot Race", "City Quarter", "Engineer", "Farmers' Market",
                                        "Forum", "Legionary", "Patrician", "Sacrifice", "Villa"],
                         event_cards=["Wedding"],
                         landmark_cards=["Tower"])]),
    Game("Advanced Intro",
         [ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Capital", "Catapult", "Crown", "Enchantress", "Gladiator",
                                        "Groundskeeper", "Royal Blacksmith", "Settlers", "Temple"],
                         landmark_cards=["Arena", "Triumphal Arch"])]),
]


class Empires(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = EMPIRES
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        self.event_cards = list(filter(lambda card: card not in banned_cards, event_cards))
        self.landmark_cards = list(filter(lambda card: card not in banned_cards, landmark_cards))
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
        return other.get_preset_(EXPANSIONS.index(EMPIRES))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=EMPIRES,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)),
                              event_cards=sorted(random.sample(self.event_cards,
                                                               min(hypergeometric(len(event_cards),
                                                                                  len(kingdom_cards) + len(event_cards),
                                                                                  self.number_of_cards),
                                                                   2))),
                              landmark_cards=sorted(random.sample(self.landmark_cards,
                                                                  min(hypergeometric(len(landmark_cards),
                                                                                     len(kingdom_cards) +
                                                                                     len(event_cards),
                                                                                     self.number_of_cards),
                                                                      2))))
