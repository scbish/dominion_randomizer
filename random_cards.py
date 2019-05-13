import random
from config import get_configuration
from game import *

first_player, expansions, banned_cards = get_configuration()

number_of_non_random_cards = sum(expansion.number_of_cards for expansion in expansions)
if number_of_non_random_cards > 10:
    raise Exception("Too many cards defined")

print()
print("Creating game with random cards from:", end=" [")
print(", ".join(expansion.name for expansion in expansions) + "]")
print("Player", first_player, "goes first")
print()
for _ in range(10 - number_of_non_random_cards):
    random.choice(expansions).number_of_cards += 1

cards = []
for expansion in expansions:
    cards.append(expansion.draw())
Game("Random Cards", list(filter(lambda card: card, cards))).print()

seaside_presets = [
    Game("Watery Graves",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Count", "Graverobber", "Hermit", "Scavenger", "Urchin"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Native Village", "Pirate Ship", "Salvager", "Treasure Map", "Treasury"])]),
    Game("Peasants",
         [ExpansionCards(name=DARK_AGES,
                         kingdom_cards=["Death Cart", "Feodum", "Poor House", "Urchin", "Vagrant"],
                         extra_cards=["Ruins"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Fishing Village", "Haven", "Island", "Lookout", "Warehouse"])]),
]

import json
import re
def p(name, first, second, first_cards, second_cards):
    first_cards = json.dumps("\", \"".join(re.compile("\t+").split(first_cards.strip()))).replace("\\", "")
    second_cards = json.dumps("\", \"".join(re.compile("\t+").split(second_cards.strip()))).replace("\\", "")
    print("    Game(\"" + name + "\",")
    print("         [ExpansionCards(name=" + first + ",")
    print("                         kingdom_cards=[" + first_cards + "]),")
    print("          ExpansionCards(name=" + second + ",")
    print("                         kingdom_cards=[" + second_cards + "])]),")
    print()
    print("    Game(\"" + name + "\",")
    print("         [ExpansionCards(name=" + second + ",")
    print("                         kingdom_cards=[" + second_cards + "]),")
    print("          ExpansionCards(name=" + first + ",")
    print("                         kingdom_cards=[" + first_cards + "])]),")


p("Son of Size Distortion",
  "DOMINION",
  "ADVENTURES",
  "		Bandit			Bureaucrat			Gardens			Moneylender			Witch",
  "	Amulet			Duplicate			Giant			Messenger			Treasure Trove	")
