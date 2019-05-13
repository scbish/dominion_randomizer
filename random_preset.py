import random
from config import get_configuration
first_player, expansions, _ = get_configuration()

print()
print("Selecting a random preset from:", end=" [")
for expansion in expansions[:-1]:
    print(expansion.name, end=", ")
print(expansions[-1].name + "]")
print("Player", first_player, "goes first")
print()
first = random.choice(expansions)
second = random.choice(expansions)
game = first.get_preset(second)
game.print()
