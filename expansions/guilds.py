from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Candlestick Maker", "Stonemason", "Doctor", "Masterpiece", "Advisor", "Plaza", "Taxman", "Herald",
                 "Baker", "Butcher", "Journeyman", "Merchant Guild", "Soothsayer"]

dominion_presets = [
    Game("Arts and Crafts",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Stonemason", "Advisor", "Baker", "Journeyman", "Merchant Guild"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Laboratory", "Cellar", "Workshop", "Festival", "Moneylender"])]),
    Game("Clean Living",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Baker", "Candlestick Maker", "Doctor", "Soothsayer"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bandit", "Militia", "Moneylender", "Gardens", "Village"])]),
    Game("Gilding the Lily",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Plaza", "Masterpiece", "Candlestick Maker", "Taxman", "Herald"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Library", "Merchant", "Remodel", "Market", "Sentry"])]),
]

intrigue_presets = [
    Game("Name That Card",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Doctor", "Plaza", "Advisor", "Masterpiece"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Courtyard", "Harem", "Nobles", "Replace", "Wishing Well"])]),
    Game("Tricks of the Trade",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Stonemason", "Herald", "Soothsayer", "Journeyman", "Butcher"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Masquerade", "Mill", "Nobles", "Secret Passage"])]),
    Game("Decisions, Decisions",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Bridge", "Pawn", "Mining Village", "Upgrade", "Duke"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Merchant Guild", "Candlestick Maker", "Masterpiece", "Taxman", "Butcher"])]),
]

seaside_presets = [
    Game("Ghosts & Taxes",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Candlestick Maker", "Herald", "Soothsayer", "Taxman"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Cutpurse", "Ghost Ship", "Haven", "Outpost", "Smugglers"])]),
    Game("Island Builder",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Doctor", "Merchant Guild", "Plaza", "Stonemason"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Island", "Native Village", "Salvager", "Tactician", "Treasury"])]),
]

alchemy_presets = [
    Game("Illuminati",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Herald", "Masterpiece", "Merchant Guild", "Stonemason"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apprentice", "Golem", "Philosopher's Stone", "Scrying Pool", "University"],
                         treasure_cards=["Potion"])]),
    Game("Tonics & Toxins",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Candlestick Maker", "Doctor", "Plaza", "Soothsayer"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Familiar", "Herbalist", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("Quarrymen",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Merchant Guild", "Soothsayer", "Stonemason", "Taxman"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["City", "Expand", "Grand Market", "Mountebank", "Quarry"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
    Game("Metal & Meat",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Candlestick Maker", "Plaza", "Stonemason", "Taxman"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Forge", "King's Court", "Monument", "Venture", "Watchtower"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
    Game("Penny Pinching",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Doctor", "Herald", "Journeyman", "Merchant Guild"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Bank", "Counting House", "Goons", "Peddler", "Royal Seal"],
                         treasure_cards=["Platinum"],
                         victory_cards=["Colony"])]),
]

cornucopia_presets = [
    Game("Misfortune",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Candlestick Maker", "Doctor", "Fairgrounds", "Farming Village"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Horse Traders", "Jester", "Soothsayer", "Taxman"])]),
    Game("Baking Contest",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Farming Village", "Harvest", "Herald", "Journeyman"]),
          ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Masterpiece", "Menagerie", "Remake", "Stonemason", "Tournament"])]),
]

hinterlands_presets = [
    Game("Exchanges",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Herald", "Masterpiece", "Soothsayer", "Stonemason"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Develop", "Ill-Gotten Gains", "Stables", "Trader"])]),
    Game("Road to Riches",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Baker", "Candlestick Maker", "Journeyman", "Merchant Guild"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Crossroads", "Farmland", "Highway", "Spice Merchant", "Tunnel"])]),
]

dark_ages_presets = [
    Game("Stoneground",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Baker", "Candlestick Maker", "Plaza", "Stonemason"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Hunting Grounds", "Ironmonger", "Procession", "Marauder", "Rogue"],
                         extra_cards=["Ruins"])]),
    Game("Class Struggle",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Butcher", "Doctor", "Journeyman", "Merchant Guild", "Taxman"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Feodum", "Fortress", "Knights", "Market Square", "Poor House"])]),
]

guilds_presets = []

adventures_presets = [
    Game("Spendthrift",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Doctor", "Masterpiece", "Merchant Guild", "Soothsayer", "Stonemason"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Artificer", "Gear", "Magpie", "Miser", "Storyteller"],
                         event_cards=["Lost Arts"])]),
    Game("Queen of Tan",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Butcher", "Candlestick Maker", "Herald", "Journeyman"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Coin of the Realm", "Duplicate", "Guide", "Ratcatcher", "Royal Carriage"],
                         event_cards=["Pathfinding", "Save"])]),
]

empires_presets = [
    Game("Cash Flow",
         [ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Butcher", "Doctor", "Herald", "Soothsayer"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Castles", "City Quarter", "Engineer", "Gladiator", "Royal Blacksmith"],
                         landmark_cards=["Baths", "Mountain Pass"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = [

]

renaissance_presets = [

]


class Guilds(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = GUILDS
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
        if isinstance(other, Guilds):
            return None
        return other.get_preset_(EXPANSIONS.index(GUILDS))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        return ExpansionCards(name=GUILDS,
                              kingdom_cards=sorted(random.sample(self.kingdom_cards, self.number_of_cards)))
