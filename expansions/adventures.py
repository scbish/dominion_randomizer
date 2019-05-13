from .expansion import Expansion
from game import *
import random

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
