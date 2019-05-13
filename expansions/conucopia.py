from .expansion import Expansion
from game import *
import random

dominion_presets = [
    Game("Bounty of the Hunt",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Harvest", "Horn of Plenty", "Hunting Party", "Menagerie", "Tournament"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Cellar", "Festival", "Militia", "Moneylender", "Smithy"])]),
    Game("Bad Omens",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Hamlet", "Horn of Plenty", "Jester", "Remake"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Bureaucrat", "Laboratory", "Merchant", "Poacher", "Throne Room"])]),
    Game("The Jester's Workshop",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Horse Traders", "Jester", "Young Witch"],
                         bane_cards=["Merchant"]),
          ExpansionCards(name=DOMINION,
                         kingdom_cards=["Artisan", "Laboratory", "Market", "Remodel", "Workshop"])]),
]

dark_ages_presets = [
    Game("Dark Carnival",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Knights", "Fairgrounds", "Hamlet", "Horn of Plenty", "Menagerie"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Band of Misfits", "Cultist", "Fortress", "Hermit", "Junk Dealer"],
                         extra_cards=["Ruins"])
          ]),
    Game("To the Victor",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Sage", "Harvest", "Hunting Party", "Remake", "Tournament"]),
          ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Bandit Camp", "Counterfeit", "Death Cart", "Marauder", "Pillage"],
                         extra_cards=["Ruins"])]),
]
