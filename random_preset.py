import random
from config import get_configuration
from expansions.alchemy import Alchemy
from expansions.conucopia import Cornucopia
from expansions.guilds import Guilds

while True:
    first_player, expansions = get_configuration(presets=True)
    if len(expansions) > 1 or not isinstance(expansions[0], (Alchemy, Cornucopia, Guilds)):
        break

print()
print("Selecting a random preset from:", end=" [")
for expansion in expansions[:-1]:
    print(expansion.name, end=", ")
print(expansions[-1].name + "]")
print("Player", first_player, "goes first")
print()
first = random.choice(expansions)
second = random.choice(expansions)
game = None
while not game:
    game = first.get_preset(second)
    first = random.choice(expansions)
    second = random.choice(expansions)
game.print()
