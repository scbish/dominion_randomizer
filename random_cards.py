import random
from config import get_configuration
from game import *

first_player, expansions = get_configuration()

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


"""
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


p("Wine & Dine",
  "CORNUCOPIA",
  "ALCHEMY",
  "\
	Fairgrounds			Hamlet			Horn of Plenty			Hunting Party			Young Witch	\
  ",
  "\
Apothecary			Apprentice			Scrying Pool			Transmute			Vineyard	\
  ")
"""