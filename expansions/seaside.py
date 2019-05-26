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

alchemy_presets = [
    Game("Forewarned",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Embargo", "Ghost Ship", "Native Village", "Treasure Map"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Golem", "Possession", "Scrying Pool", "Transmute"],
                         treasure_cards=["Potion"])]),
    Game("Gummed Up",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Haven", "Sea Hag", "Smugglers", "Warehouse"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Familiar", "Herbalist", "Philosopher's Stone", "Vineyard"],
                         treasure_cards=["Potion"])]),
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

cornucopia_presets = [
    Game("Collector",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Embargo", "Fishing Village", "Merchant Ship", "Navigator", "Smugglers"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Fortune Teller", "Harvest",
                                        "Hunting Party"])]),
    Game("Collider",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Lighthouse", "Salvager", "Treasure Map", "Treasury", "Warehouse"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Menagerie", "Horn of Plenty", "Horse Traders", "Jester", "Tournament"])]),
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

guilds_presets = [
    Game("Ghosts & Taxes",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Ghost Ship", "Haven", "Outpost", "Smugglers"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Candlestick Maker", "Herald", "Soothsayer", "Taxman"])]),
    Game("Island Builder",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Island", "Native Village", "Salvager", "Tactician", "Treasury"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Doctor", "Merchant Guild", "Plaza", "Stonemason"])]),
]

adventures_presets = [
    Game("Prince of Orange",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Caravan", "Fishing Village", "Merchant Ship", "Tactician", "Treasure Map"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Dungeon", "Haunted Woods", "Page", "Swamp Hag"],
                         event_cards=["Mission"])]),
    Game("Gifts and Mathoms",
         [ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Embargo", "Haven", "Salvager", "Smugglers"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Bridge Troll", "Caravan Guard", "Hireling", "Lost City", "Messenger"],
                         event_cards=["Expedition", "Quest"])]),
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

# TODO: nocturne/renaissance support
nocturne_presets = []

renaissance_presets = []


class Seaside(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = SEASIDE
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
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
        return other.get_preset_(EXPANSIONS.index(SEASIDE))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=SEASIDE,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
