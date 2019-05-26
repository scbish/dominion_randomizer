from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Herbalist", "Apprentice", "Transmute", "Vineyard", "Apothecary", "Scrying Pool", "University",
                 "Alchemist", "Familiar", "Philosopher's Stone", "Golem", "Possession"]

dominion_presets = [
    Game("Forbidden Arts",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Familiar", "Possession", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Cellar", "Council Room", "Gardens", "Laboratory", "Throne Room"])]),
    Game("Potion Mixers",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Apothecary", "Golem", "Herbalist", "Transmute"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Militia", "Poacher", "Smithy"])]),
    Game("Chemistry Lesson",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Golem", "Philosopher's Stone", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Market", "Moat", "Remodel", "Vassal", "Witch"])]),
]

intrigue_presets = [
    Game("Servants",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Golem", "Possession", "Scrying Pool", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Mill", "Minion", "Pawn", "Steward"])]),
    Game("Secret Research",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Familiar", "Herbalist", "Philosopher's Stone", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Bridge", "Masquerade", "Minion", "Nobles", "Shanty Town", "Torturer"])]),
    Game("Pools, Tools, and Fools",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Apprentice", "Golem", "Scrying Pool"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Baron", "Ironworks", "Lurker", "Nobles", "Trading Post", "Wishing Well"])]),
]

seaside_presets = [
    Game("Forewarned",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Golem", "Possession", "Scrying Pool", "Transmute"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Embargo", "Ghost Ship", "Native Village", "Treasure Map"])]),
    Game("Gummed Up",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Familiar", "Herbalist", "Philosopher's Stone", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Ambassador", "Haven", "Sea Hag", "Smugglers", "Warehouse"])]),
]

alchemy_presets = []

prosperity_presets = [
    Game("Counting Contest",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Philosopher's Stone", "Golem", "Herbalist", "Apothecary"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Counting House", "Hoard", "Goons", "Rabble", "Quarry"])]),
    Game("Lower Learning",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Familiar", "Apprentice", "University", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Talisman", "Mint", "Bishop", "Worker's Village", "Peddler", "Vault"])]),
]

cornucopia_presets = [
    Game("Clown College",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Familiar", "Golem", "Philosopher's Stone", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Harvest", "Horse Traders", "Jester", "Menagerie", "Remake"])]),
    Game("Wine & Dine",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Apprentice", "Scrying Pool", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Hamlet", "Horn of Plenty", "Hunting Party", "Young Witch"],
                         bane_cards=["Herbalist"])]),
]

hinterlands_presets = [
    Game("Schemes and Dreams",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Apprentice", "Herbalist", "Philosopher's Stone", "Transmute"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Duchess", "Fool's Gold", "Ill-Gotten Gains", "Jack of all Trades",
                                        "Scheme"])]),
    Game("Wine Country",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Familiar", "Golem", "University", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Haggler", "Highway", "Nomad Camp"])]),
]

dark_ages_presets = [
    Game("Infestations",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Scrying Pool", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Armory", "Cultist", "Feodum", "Market Square", "Rats", "Wandering Minstrel"],
                         extra_cards=["Ruins"])]),
    Game("Lamentations",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Golem", "Herbalist", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Beggar", "Catacombs", "Counterfeit", "Forager", "Ironmonger", "Pillage"])]),
]

guilds_presets = [
    Game("Illuminati",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Golem", "Philosopher's Stone", "Scrying Pool", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Herald", "Masterpiece", "Merchant Guild", "Stonemason"])]),
    Game("Tonics & Toxins",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Familiar", "Herbalist", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Candlestick Maker", "Doctor", "Plaza", "Soothsayer"])]),
]

adventures_presets = [
    Game("Haste Potion",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Scrying Pool", "Transmute", "University", "Vineyard"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Magpie", "Messenger", "Port", "Royal Carriage", "Treasure Trove"],
                         event_cards=["Plan"])]),
    Game("Cursecatchers",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Familiar", "Golem", "Herbalist", "Philosopher's Stone"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Amulet", "Bridge Troll", "Caravan Guard", "Peasant", "Ratcatcher"],
                         event_cards=["Save", "Trade"])]),
]

empires_presets = [
    Game("Collectors",
         [ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Apprentice", "Herbalist", "Transmute", "University"],
                         treasure_cards=["Potion"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["City Quarter", "Crown", "Encampment", "Enchantress", "Farmers' Market"],
                         landmark_cards=["Colonnade", "Museum"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = [

]

renaissance_presets = [

]


class Alchemy(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = ALCHEMY
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
        if isinstance(other, Alchemy):
            return None
        return other.get_preset_(EXPANSIONS.index(ALCHEMY))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=ALCHEMY,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)),
                              treasure_cards=["Potion"])
