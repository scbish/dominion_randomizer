from .expansion import Expansion
from game import *
import random
from numpy.random import hypergeometric

kingdom_cards = ["Coin of the Realm", "Page", "Peasant", "Ratcatcher", "Raze", "Amulet", "Caravan Guard", "Dungeon",
                 "Gear", "Guide", "Duplicate", "Magpie", "Messenger", "Miser", "Port", "Ranger", "Transmogrify",
                 "Artificer", "Bridge Troll", "Distant Lands", "Giant", "Haunted Woods", "Lost City", "Relic",
                 "Royal Carriage", "Storyteller", "Swamp Hag", "Treasure Trove", "Wine Merchant", "Hireling"]

event_cards = ["Alms", "Borrow", "Quest", "Save", "Scouting Party", "Travelling Fair", "Bonfire", "Expedition", "Ferry",
               "Plan", "Mission", "Pilgrimage", "Ball", "Raid", "Seaway", "Trade", "Lost Arts", "Training",
               "Inheritance", "Pathfinding"]

dominion_presets = [
    Game("Level Up",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Dungeon", "Gear", "Guide", "Lost City", "Miser"],
                         event_cards=["Training"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Market", "Merchant", "Militia", "Throne Room", "Workshop"])]),
    Game("Son of Size Distortion",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Duplicate", "Giant", "Messenger", "Treasure Trove"],
                         event_cards=["Bonfire", "Raid"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Bureaucrat", "Gardens", "Moneylender", "Witch"])]),
]

intrigue_presets = [
    Game("Royalty Factory",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Bridge Troll", "Duplicate", "Page", "Raze", "Royal Carriage"],
                         event_cards=["Pilgrimage"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Courtier", "Harem", "Nobles", "Swindler"])]),
    Game("Masters of Finance",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Artificer", "Distant Lands", "Gear", "Transmogrify", "Wine Merchant"],
                         event_cards=["Ball", "Borrow"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Pawn", "Shanty Town", "Steward", "Upgrade"])]),
]

seaside_presets = [
    Game("Prince of Orange",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Dungeon", "Haunted Woods", "Page", "Swamp Hag"],
                         event_cards=["Mission"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Caravan", "Fishing Village", "Merchant Ship", "Tactician", "Treasure Map"])]),
    Game("Gifts and Mathoms",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Bridge Troll", "Caravan Guard", "Hireling", "Lost City", "Messenger"],
                         event_cards=["Expedition", "Quest"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Embargo", "Haven", "Salvager", "Smugglers"])]),
]

alchemy_presets = [
    Game("Haste Potion",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Magpie", "Messenger", "Port", "Royal Carriage", "Treasure Trove"],
                         event_cards=["Plan"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Scrying Pool", "Transmute", "University", "Vineyard"],
                         treasure_cards=["Potion"])]),
    Game("Cursecatchers",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Bridge Troll", "Caravan Guard", "Peasant", "Ratcatcher"],
                         event_cards=["Save", "Trade"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Familiar", "Golem", "Herbalist", "Philosopher's Stone"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("Last Will and Monument",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Coin of the Realm", "Dungeon", "Messenger", "Relic", "Treasure Trove"],
                         event_cards=["Inheritance"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Counting House", "Monument", "Rabble", "Vault"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
    Game("Think Big",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Distant Lands", "Giant", "Hireling", "Miser", "Storyteller"],
                         event_cards=["Ball", "Ferry"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Contraband", "Expand", "Hoard", "King's Court", "Peddler"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
]

cornucopia_presets = [
    Game("The Hero's Return",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Horse Traders", "Jester", "Menagerie"],
                         event_cards=["Travelling Fair"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Artificer", "Miser", "Page", "Ranger", "Relic"])]),
    Game("Seacraft and Witchcraft",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Peasant", "Storyteller", "Swamp Hag", "Transmogrify", "Wine Merchant"],
                         event_cards=["Ferry", "Seaway"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Hamlet", "Horn of Plenty", "Tournament", "Young Witch"],
                         bane_cards=["Guide"])]),
]

hinterlands_presets = [
    Game("Traders and Raiders",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Haunted Woods", "Lost City", "Page", "Port", "Wine Merchant"],
                         event_cards=["Raid"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Develop", "Farmland", "Haggler", "Spice Merchant", "Trader"])]),
    Game("Journeys",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Bridge Troll", "Distant Lands", "Giant", "Guide", "Ranger"],
                         event_cards=["Expedition", "Inheritance"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cartographer", "Crossroads", "Highway", "Inn", "Silk Road"])]),
]

dark_ages_presets = [
    Game("Cemetery Polka",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Caravan Guard", "Hireling", "Peasant", "Relic"],
                         event_cards=["Alms"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Graverobber", "Marauder", "Procession", "Rogue", "Wandering Minstrel"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"])]),
    Game("Groovy Decay",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Dungeon", "Haunted Woods", "Ratcatcher", "Raze", "Transmogrify"],
                         event_cards=["Lost Arts", "Pathfinding"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Cultist", "Death Cart", "Fortress", "Knights", "Rats"],
                         starter_cards=["Shelters"],
                         extra_cards=["Ruins"])]),
]

guilds_presets = [
    Game("Spendthrift",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Artificer", "Gear", "Magpie", "Miser", "Storyteller"],
                         event_cards=["Lost Arts"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Doctor", "Masterpiece", "Merchant Guild", "Soothsayer", "Stonemason"])]),
    Game("Queen of Tan",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Coin of the Realm", "Duplicate", "Guide", "Ratcatcher", "Royal Carriage"],
                         event_cards=["Pathfinding", "Save"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Butcher", "Candlestick Maker", "Herald", "Journeyman"])]),
]

adventures_presets = [
    Game("Gentle Intro",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Distant Lands", "Dungeon", "Duplicate", "Giant", "Hireling", "Port",
                                        "Ranger", "Ratcatcher", "Treasure Trove"],
                         event_cards=["Scouting Party"])]),
    Game("Expert Intro",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Caravan Guard", "Coin of the Realm", "Haunted Woods", "Lost City", "Magpie",
                                        "Peasant", "Raze", "Swamp Hag", "Transmogrify", "Wine Merchant"],
                         event_cards=["Mission", "Plan"])]),
]

empires_presets = [
    Game("Area Control",
         [ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Coin of the Realm", "Page", "Relic", "Treasure Trove", "Wine Merchant"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Capital", "Catapult", "Charm", "Crown", "Farmers' Market"],
                         event_cards=["Banquet"],
                         landmark_cards=["Keep"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = [

]

renaissance_presets = [

]


class Adventures(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = ADVENTURES
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        self.event_cards = list(filter(lambda card: card not in banned_cards, event_cards))
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
        return other.get_preset_(EXPANSIONS.index(ADVENTURES))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=ADVENTURES,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)),
                              event_cards=sorted(random.sample(self.event_cards,
                                                               min(hypergeometric(len(event_cards),
                                                                                  len(kingdom_cards) + len(event_cards),
                                                                                  self.number_of_cards),
                                                                   2))))
