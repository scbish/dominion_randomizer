from .expansion import Expansion
from game import *
import random

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
