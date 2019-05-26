import random
from expansions.dominion import Dominion
from expansions.intrigue import Intrigue
from expansions.seaside import Seaside
from expansions.alchemy import Alchemy
from expansions.prosperity import Prosperity
from expansions.conucopia import Cornucopia
from expansions.hinterlands import Hinterlands
from expansions.guilds import Guilds
from expansions.adventures import Adventures
from expansions.dark_ages import DarkAges
from expansions.empires import Empires
from expansions.nocturne import Nocturne
from expansions.renaissance import Renaissance

number_of_players = 4

banned_cards = [
    "Bandit",
    "Treasure Map",
    "Noble Brigand",
    "Pirate Ship",
]

expansions = [
    # Dominion(0, banned_cards),
    # Intrigue(0, banned_cards),
    # Seaside(0, banned_cards),
    # Alchemy(0, banned_cards),
    # Prosperity(0, banned_cards),
    Cornucopia(0, banned_cards),
    # Hinterlands(0, banned_cards),
    # DarkAges(0, banned_cards),
    Guilds(0, banned_cards),
    # Adventures(0, banned_cards),
    # Empires(0, banned_cards),
    # Nocturne(0, banned_cards),
    # Renaissance(0, banned_cards)
]

random_games = False
min_number_of_games = 2
max_number_of_games = 2


def get_configuration(presets=False):
    if presets and len(expansions) == 1 and isinstance(expansions[0], (Alchemy, Cornucopia, Guilds)):
        raise Exception("No presets for only Alchemy, Cornucopia, or Guilds")
    if random_games:
        if max_number_of_games < min_number_of_games or min_number_of_games < 1:
            raise Exception("Invalid range: {} - {}".format(min_number_of_games, max_number_of_games))
        if len(expansions) < min_number_of_games:
            raise Exception(
                "Not enough games to choose from: {} games, {} specified".format(len(expansions), min_number_of_games))
        selected_expansions = random.sample(expansions, random.randint(min_number_of_games, max_number_of_games))
    else:
        if not expansions:
            raise Exception("No expansions were selected")
        selected_expansions = expansions
    return random.randint(1, number_of_players), selected_expansions
