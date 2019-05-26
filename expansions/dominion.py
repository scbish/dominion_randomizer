from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Cellar", "Chapel", "Moat", "Harbinger", "Merchant", "Vassal", "Village", "Workshop", "Bureaucrat",
                 "Gardens", "Militia", "Moneylender", "Poacher", "Remodel", "Smithy", "Throne Room", "Bandit",
                 "Council Room", "Festival", "Laboratory", "Library", "Market", "Mine", "Sentry", "Witch", "Artisan"]

dominion_presets = [
    Game("First Game",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Market", "Merchant", "Militia", "Mine", "Moat", "Remodel", "Smithy",
                                        "Village", "Workshop"])]),
    Game("Size Distortion",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Bandit", "Bureaucrat", "Chapel", "Festival", "Gardens", "Sentry",
                                        "Throne Room", "Witch", "Workshop"])]),
    Game("Deck Top",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Bureaucrat", "Council Room", "Festival", "Harbinger", "Laboratory",
                                        "Moneylender", "Sentry", "Vassal", "Village"])]),
    Game("Sleight of Hand",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Council Room", "Festival", "Gardens", "Library", "Harbinger",
                                        "Militia", "Poacher", "Smithy", "Throne Room"])]),
    Game("Improvements",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Cellar", "Market", "Merchant", "Mine", "Moat", "Moneylender",
                                        "Poacher", "Remodel", "Witch"])]),
    Game("Silver & Gold",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Bureaucrat", "Chapel", "Harbinger", "Laboratory", "Merchant", "Mine",
                                        "Moneylender", "Throne Room", "Vassal"])]),
]

intrigue_presets = [
    Game("Underlings",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Library", "Sentry", "Vassal"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Courtier", "Diplomat", "Minion", "Nobles", "Pawn"])]),
    Game("Grand Scheme",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Council Room", "Market", "Militia", "Workshop"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Mill", "Mining Village", "Patrol", "Shanty Town"])]),
    Game("Deconstruction",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Mine", "Remodel", "Throne Room", "Village"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Diplomat", "Harem", "Lurker", "Replace", "Swindler"])]),
]

seaside_presets = [
    Game("Reach for Tomorrow",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Cellar", "Council Room", "Vassal", "Village"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Ghost Ship", "Lookout", "Sea Hag", "Treasure Map"])]),
    Game("Repetition",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Harbinger", "Militia", "Workshop", "Caravan"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Explorer", "Outpost", "Pearl Diver", "Pirate Ship", "Treasury"])]),
    Game("Give and Take",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Library", "Market", "Moneylender", "Witch", "Ambassador"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Haven", "Island", "Salvager", "Smugglers"])]),
]

alchemy_presets = [
    Game("Forbidden Arts",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Cellar", "Council Room", "Gardens", "Laboratory", "Throne Room"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Familiar", "Possession", "University"],
                         treasure_cards=["Potion"])]),
    Game("Potion Mixers",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Militia", "Poacher", "Smithy"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Apothecary", "Golem", "Herbalist", "Transmute"],
                         treasure_cards=["Potion"])]),
    Game("Chemistry Lesson",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Market", "Moat", "Remodel", "Vassal", "Witch"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Golem", "Philosopher's Stone", "University"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("Biggest Money",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Harbinger", "Laboratory", "Mine", "Moneylender"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Grand Market", "Mint", "Royal Seal", "Venture"])]),
    Game("The King's Army",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Council Room", "Merchant", "Moat", "Village"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Expand", "Goons", "King's Court", "Rabble", "Vault"])]),
    Game("The Good Life",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Bureaucrat", "Cellar", "Gardens", "Village"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Contraband", "Counting House", "Hoard", "Monument", "Mountebank"])]),
]

cornucopia_presets = [
    Game("Bounty of the Hunt",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Militia", "Moneylender", "Smithy"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Harvest", "Horn of Plenty", "Hunting Party", "Menagerie", "Tournament"])]),
    Game("Bad Omens",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Laboratory", "Merchant", "Poacher", "Throne Room"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Hamlet", "Horn of Plenty", "Jester", "Remake"])]),
    Game("The Jester's Workshop",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Laboratory", "Market", "Remodel", "Workshop"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Horse Traders", "Jester", "Young Witch"],
                         bane_cards=["Merchant"])]),
]

hinterlands_presets = [
    Game("Highway Robbery",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Library", "Moneylender", "Throne Room", "Workshop"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Highway", "Inn", "Margrave", "Noble Brigand", "Oasis"])]),
    Game("Adventures Abroad",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Laboratory", "Remodel", "Sentry", "Vassal"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Fool's Gold", "Oracle", "Spice Merchant"])]),
]

dark_ages_presets = [
    Game("High and Low",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Moneylender", "Throne Room", "Witch", "Workshop"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Hermit", "Hunting Grounds", "Mystic", "Poor House", "Wandering Minstrel"])]),
    Game("Chivalry and Revelry",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Festival", "Gardens", "Laboratory", "Library", "Remodel"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Altar", "Knights", "Rats", "Scavenger", "Squire"])]),
]

guilds_presets = [
    Game("Arts and Crafts",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Laboratory", "Cellar", "Workshop", "Festival", "Moneylender"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Stonemason", "Advisor", "Baker", "Journeyman", "Merchant Guild"])]),
    Game("Clean Living",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Militia", "Moneylender", "Gardens", "Village"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Baker", "Candlestick Maker", "Doctor", "Soothsayer"])]),
    Game("Gilding the Lily",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Library", "Merchant", "Remodel", "Market", "Sentry"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Plaza", "Masterpiece", "Candlestick Maker", "Taxman", "Herald"])]),
]

adventures_presets = [
    Game("Level Up",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Market", "Merchant", "Militia", "Throne Room", "Workshop"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Dungeon", "Gear", "Guide", "Lost City", "Miser"],
                         event_cards=["Training"])]),
    Game("Son of Size Distortion",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Bureaucrat", "Gardens", "Moneylender", "Witch"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Duplicate", "Giant", "Messenger", "Treasure Trove"],
                         event_cards=["Bonfire", "Raid"])]),
]

empires_presets = [
    Game("Everything in Moderation",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Library", "Remodel", "Village", "Workshop"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Enchantress", "Forum", "Legionary", "Overlord", "Temple"],
                         event_cards=["Windfall"],
                         landmark_cards=["Orchard"])]),
    Game("Silver Bullets",
         [ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Gardens", "Laboratory", "Market", "Moneylender"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Catapult", "Charm", "Farmers' Market", "Groundskeeper", "Patrician"],
                         event_cards=["Conquest"],
                         landmark_cards=["Aqueduct"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = []

renaissance_presets = []


class Dominion(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = DOMINION
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
        return other.get_preset_(EXPANSIONS.index(DOMINION))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=DOMINION,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
