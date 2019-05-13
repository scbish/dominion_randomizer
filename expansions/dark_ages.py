from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Poor House", "Beggar", "Squire", "Vagrant", "Forager", "Hermit", "Market Square", "Sage", "Storeroom",
                 "Urchin", "Armory", "Death Cart", "Feodum", "Fortress", "Ironmonger", "Marauder", "Procession", "Rats",
                 "Scavenger", "Wandering Minstrel", "Band of Misfits", "Bandit Camp", "Catacombs", "Count",
                 "Counterfeit", "Cultist", "Graverobber", "Junk Dealer", "Knights", "Mystic", "Pillage", "Rebuild",
                 "Rogue", "Altar", "Hunting Grounds"]
starter_cards = ["Shelters"]
extra_cards = ["Ruins"]

dominion_presets = [
    Game("High and Low",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Hermit", "Hunting Grounds", "Mystic", "Poor House", "Wandering Minstrel"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Moneylender", "Throne Room", "Witch", "Workshop"])]),
    Game("Chivalry and Revelry",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Altar", "Knights", "Rats", "Scavenger", "Squire"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Gardens", "Laboratory", "Library", "Remodel"])]),
]

intrigue_presets = [
    Game("Prophecy",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Armory", "Ironmonger", "Mystic", "Rebuild", "Vagrant"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Conspirator", "Nobles", "Secret Passage", "Wishing Well"])]),
    Game("Invasion",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Beggar", "Marauder", "Rogue", "Squire", "Urchin"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Diplomat", "Harem", "Swindler", "Torturer", "Upgrade"])]),
]

seaside_presets = [
    Game("Watery Graves",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Count", "Graverobber", "Hermit", "Scavenger", "Urchin"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Native Village", "Pirate Ship", "Salvager", "Treasure Map", "Treasury"])]),
    Game("Peasants",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Death Cart", "Feodum", "Poor House", "Urchin", "Vagrant"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Haven", "Island", "Lookout", "Warehouse"])]),
]

alchemy_presets = [
    Game("Infestations",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Cultist", "Feodum", "Market Square", "Rats", "Wandering Minstrel"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Scrying Pool", "Transmute", "Vineyard", "Armory"],
                         treasure_cards=["Potion"])]),
    Game("Lamentations",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Catacombs", "Counterfeit", "Forager", "Ironmonger", "Pillage"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Golem", "Herbalist", "University", "Beggar"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("One Man's Trash",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Counterfeit", "Forager", "Graverobber", "Market Square", "Rogue"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["City", "Grand Market", "Monument", "Talisman", "Venture"])]),
    Game("Honor Among Thieves",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Procession", "Rebuild", "Rogue", "Squire"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Forge", "Hoard", "Peddler", "Quarry", "Watchtower"])]),
]

cornucopia_presets = [
    Game("Dark Carnival",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Band of Misfits", "Cultist", "Fortress", "Hermit", "Junk Dealer"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Knights", "Fairgrounds", "Hamlet", "Horn of Plenty", "Menagerie"])]),
    Game("To the Victor",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Counterfeit", "Death Cart", "Marauder", "Pillage"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Sage", "Harvest", "Hunting Party", "Remake", "Tournament"])]),
]

hinterlands_presets = [
    Game("Far From Home",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Beggar", "Count", "Feodum", "Marauder", "Wandering Minstrel"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Develop", "Embassy", "Fool's Gold", "Haggler"])]),
    Game("Expeditions",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Altar", "Catacombs", "Ironmonger", "Poor House", "Storeroom"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Highway", "Spice Merchant", "Tunnel"])]),
]

dark_ages_presets = [
    Game("Grim Parade",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Armory", "Band of Misfits", "Catacombs", "Cultist", "Forager", "Fortress",
                                        "Hunting Grounds", "Knights", "Market Square", "Procession"],
                         extra_cards=["Ruins"])]),
    Game("Chess With Death",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Graverobber", "Junk Dealer", "Mystic", "Pillage", "Rats",
                                        "Sage", "Scavenger", "Storeroom", "Vagrant"])]),
]

guilds_presets = [
    Game("Stoneground",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Hunting Grounds", "Ironmonger", "Procession", "Marauder", "Rogue"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Baker", "Candlestick Maker", "Plaza", "Stonemason"])]),
    Game("Class Struggle",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Feodum", "Fortress", "Knights", "Market Square", "Poor House"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Doctor", "Journeyman", "Merchant Guild", "Taxman"])]),
]

adventures_presets = [
    Game("Cemetery Polka",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Graverobber", "Marauder", "Procession", "Rogue", "Wandering Minstrel"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Caravan Guard", "Hireling", "Peasant", "Relic"],
                         event_cards=["Alms"])]),
    Game("Groovy Decay",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Cultist", "Death Cart", "Fortress", "Knights", "Rats"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Dungeon", "Haunted Woods", "Ratcatcher", "Raze", "Transmogrify"],
                         event_cards=["Lost Arts", "Pathfinding"])]),
]

empires_presets = [
    Game("Tomb of the Rat King",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Death Cart", "Fortress", "Pillage", "Rats", "Storeroom"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "Chariot Race", "City Quarter", "Legionary", "Sacrifice"],
                         event_cards=["Advance"],
                         landmark_cards=["Tomb"])]),
    Game("Triumph of the Bandit King",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Catacombs", "Hunting Grounds", "Market Square", "Procession"],
                         starter_cards=["Shelters"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Capital", "Charm", "Engineer", "Groundskeeper", "Legionary"],
                         event_cards=["Triumph"],
                         landmark_cards=["Defiled Shrine"])]),
    Game("The Squire's Ritual",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Feodum", "Hermit", "Ironmonger", "Rogue", "Squire"],
                         starter_cards=["Shelters"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Archive", "Catapult", "Crown", "Patrician", "Settlers"],
                         event_cards=["Ritual"],
                         landmark_cards=["Museum"])]),
]

nocturne_presets = []

renaissance_presets = []


class DarkAges(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = DARK_AGES
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        self.starter_cards = list(filter(lambda card: card not in banned_cards, starter_cards))
        self.extra_cards = list(filter(lambda card: card not in banned_cards, extra_cards))
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
        return other.get_preset_(EXPANSIONS.index(DARK_AGES))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=DARK_AGES,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)),
                              starter_cards=starter_cards if random.randint(0, 9) < self.number_of_cards else None,
                              extra_cards=extra_cards if random.randint(0, 9) < self.number_of_cards else None)
