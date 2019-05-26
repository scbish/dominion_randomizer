from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Loan", "Trade Route", "Watchtower", "Bishop", "Monument", "Quarry", "Talisman", "Worker's Village",
                 "City", "Contraband", "Counting House", "Mint", "Mountebank", "Rabble", "Royal Seal", "Vault",
                 "Venture", "Goons", "Grand Market", "Hoard", "Bank", "Expand", "Forge", "King's Court", "Peddler"]
treasure_cards = ["Platinum"]
victory_cards = ["Colony"]

dominion_presets = [
    Game("Biggest Money",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Grand Market", "Mint", "Royal Seal", "Venture"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Harbinger", "Laboratory", "Mine", "Moneylender"])]),
    Game("The King's Army",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Expand", "Goons", "King's Court", "Rabble", "Vault"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Council Room", "Merchant", "Moat", "Village"])]),
    Game("The Good Life",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Contraband", "Counting House", "Hoard", "Monument", "Mountebank"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Bureaucrat", "Cellar", "Gardens", "Village"])]),
]

intrigue_presets = [
    Game("Paths to Victory",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Counting House", "Goons", "Monument", "Peddler"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Harem", "Pawn", "Shanty Town", "Upgrade"])]),
    Game("All Along the Watchtower",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Hoard", "Talisman", "Trade Route", "Vault", "Watchtower"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Mill", "Mining Village", "Pawn", "Torturer"])]),
    Game("Lucky Seven",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Expand", "Forge", "King's Court", "Vault"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Lurker", "Patrol", "Swindler", "Wishing Well"])]),
]

seaside_presets = [
    Game("Exploding Kingdom",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "City", "Grand Market", "King's Court", "Quarry"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Lookout", "Outpost", "Tactician", "Wharf"])]),
    Game("Pirate Bay",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Expand", "Hoard", "Mint", "Trade Route", "Watchtower"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Bazaar", "Lighthouse", "Pirate Ship", "Smugglers", "Warehouse"])]),
]

alchemy_presets = [
    Game("Counting Contest",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Counting House", "Hoard", "Goons", "Rabble", "Quarry"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Philosopher's Stone", "Golem", "Herbalist", "Apothecary"],
                         treasure_cards=["Potion"])]),
    Game("Lower Learning",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Talisman", "Mint", "Bishop", "Worker's Village", "Peddler", "Vault"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Familiar", "Apprentice", "University", "Vineyard"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("Beginners",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Counting House", "Expand", "Goons", "Monument", "Rabble", "Royal Seal",
                                        "Venture", "Watchtower", "Worker's Village"])]),
    Game("Friendly Interactive",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "City", "Contraband", "Forge", "Hoard", "Peddler", "Royal Seal",
                                        "Trade Route", "Vault", "Worker's Village"])]),
    Game("Big Actions",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["City", "Expand", "Grand Market", "King's Court", "Loan", "Mint", "Quarry",
                                        "Rabble", "Talisman", "Vault"])]),
]

cornucopia_presets = [
    Game("Detours",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Rabble", "Peddler", "Hoard", "Trade Route", "Venture"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Farming Village", "Horn of Plenty", "Jester", "Remake", "Tournament"])]),
]

hinterlands_presets = [
    Game("Instant Gratification",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Expand", "Hoard", "Mint", "Watchtower"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Farmland", "Haggler", "Ill-Gotten Gains", "Noble Brigand", "Trader"])]),
    Game("Treasure Trove",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Monument", "Royal Seal", "Trade Route", "Venture"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Cache", "Develop", "Fool's Gold", "Ill-Gotten Gains", "Mandarin"])]),
]

dark_ages_presets = [
    Game("One Man's Trash",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Counterfeit", "Forager", "Graverobber", "Market Square", "Rogue"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["City", "Grand Market", "Monument", "Talisman", "Venture"])]),
    Game("Honor Among Thieves",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bandit Camp", "Procession", "Rebuild", "Rogue", "Squire"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Forge", "Hoard", "Peddler", "Quarry", "Watchtower"])]),
]

guilds_presets = [
    Game("Quarrymen",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["City", "Expand", "Grand Market", "Mountebank", "Quarry"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Merchant Guild", "Soothsayer", "Stonemason", "Taxman"])]),
    Game("Metal & Meat",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Forge", "King's Court", "Monument", "Venture", "Watchtower"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Candlestick Maker", "Plaza", "Stonemason", "Taxman"])]),
    Game("Penny Pinching",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Counting House", "Goons", "Peddler", "Royal Seal"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Doctor", "Herald", "Journeyman", "Merchant Guild"])]),
]

adventures_presets = [
    Game("Last Will and Monument",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Counting House", "Monument", "Rabble", "Vault"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Coin of the Realm", "Dungeon", "Messenger", "Relic", "Treasure Trove"],
                         event_cards=["Inheritance"])]),
    Game("Think Big",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Contraband", "Expand", "Hoard", "King's Court", "Peddler"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Distant Lands", "Giant", "Hireling", "Miser", "Storyteller"],
                         event_cards=["Ball", "Ferry"])]),
]

empires_presets = [
    Game("Big Time",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Forge", "Grand Market", "Loan", "Royal Seal"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Capital", "Gladiator", "Patrician", "Royal Blacksmith", "Villa"],
                         event_cards=["Dominate"],
                         landmark_cards=["Obelisk"])]),
    Game("Gilded Gates",
         [ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bishop", "Monument", "Mint", "Peddler", "Talisman"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Chariot Race", "City Quarter", "Encampment", "Groundskeeper", "Wild Hunt"],
                         landmark_cards=["Basilica", "Palace"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = []

renaissance_presets = []


class Prosperity(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = PROSPERITY
        self.kingdom_cards = list(filter(lambda card: card not in banned_cards, kingdom_cards))
        self.treasure_cards = list(filter(lambda card: card not in banned_cards, treasure_cards))
        self.victory_cards = list(filter(lambda card: card not in banned_cards, victory_cards))
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
        return other.get_preset_(EXPANSIONS.index(PROSPERITY))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        unique_cards = random.randint(0, 9) < self.number_of_cards
        return ExpansionCards(name=PROSPERITY,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)),
                              treasure_cards=treasure_cards if unique_cards else None,
                              victory_cards=victory_cards if unique_cards else None)
