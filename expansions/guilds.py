from .expansion import Expansion
from game import *
import random

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
