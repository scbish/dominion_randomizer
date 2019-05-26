from .expansion import Expansion
from game import *
import random

kingdom_cards = ["Hamlet", "Fortune Teller", "Menagerie", "Farming Village", "Horse Traders", "Remake", "Tournament",
                 "Young Witch", "Harvest", "Horn of Plenty", "Hunting Party", "Jester", "Fairgrounds"]

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

intrigue_presets = [
    Game("Last Laughs",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Farming Village", "Harvest", "Horse Traders", "Hunting Party", "Jester"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Minion", "Nobles", "Pawn", "Steward", "Swindler"])]),
    Game("The Spice of Life",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Courtier", "Courtyard", "Diplomat", "Mining Village", "Replace"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Fairgrounds", "Horn of Plenty", "Remake", "Tournament", "Young Witch"],
                         bane_cards=["Wishing Well"])]),
    Game("Small Victories",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Hamlet", "Hunting Party", "Remake", "Tournament"]),
          ExpansionCards(name=INTRIGUE,
                         kingdom_cards=["Conspirator", "Duke", "Harem", "Pawn", "Secret Passage"])]),
]

seaside_presets = [
    Game("Collector",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Fortune Teller", "Harvest",
                                        "Hunting Party"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Embargo", "Fishing Village", "Merchant Ship", "Navigator", "Smugglers"])]),
    Game("Collider",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Menagerie", "Horn of Plenty", "Horse Traders", "Jester", "Tournament"]),
          ExpansionCards(name=SEASIDE,
                         kingdom_cards=["Lighthouse", "Salvager", "Treasure Map", "Treasury", "Warehouse"])]),
]

alchemy_presets = [
    Game("Clown College",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Harvest", "Horse Traders", "Jester", "Menagerie", "Remake"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Alchemist", "Familiar", "Golem", "Philosopher's Stone", "University"],
                         treasure_cards=["Potion"])]),
    Game("Wine & Dine",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Hamlet", "Horn of Plenty", "Hunting Party", "Young Witch"],
                         bane_cards=["Herbalist"]),
          ExpansionCards(name=ALCHEMY,
                         kingdom_cards=["Apothecary", "Apprentice", "Scrying Pool", "Transmute", "Vineyard"],
                         treasure_cards=["Potion"])]),
]

prosperity_presets = [
    Game("Detours",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Farming Village", "Horn of Plenty", "Jester", "Remake", "Tournament"]),
          ExpansionCards(name=PROSPERITY,
                         kingdom_cards=["Rabble", "Peddler", "Hoard", "Trade Route", "Venture"])]),
]

cornucopia_presets = []

hinterlands_presets = [
    Game("Blue Harvest",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Hamlet", "Horn of Plenty", "Horse Traders", "Jester", "Tournament"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Fool's Gold", "Mandarin", "Noble Brigand", "Trader", "Tunnel"])]),
    Game("Traveling Circus",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Hunting Party", "Jester", "Menagerie"]),
          ExpansionCards(name=HINTERLANDS,
                         kingdom_cards=["Border Village", "Embassy", "Fool's Gold", "Nomad Camp", "Oasis"])]),
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

guilds_presets = [
    Game("Misfortune",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Horse Traders", "Jester", "Soothsayer", "Taxman"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Advisor", "Candlestick Maker", "Doctor", "Fairgrounds", "Farming Village"])]),
    Game("Baking Contest",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Masterpiece", "Menagerie", "Remake", "Stonemason", "Tournament"]),
          ExpansionCards(name=GUILDS,
                         kingdom_cards=["Baker", "Farming Village", "Harvest", "Herald", "Journeyman"])]),
]

adventures_presets = [
    Game("The Hero's Return",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Artificer", "Miser", "Page", "Ranger", "Relic"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Fairgrounds", "Farming Village", "Horse Traders", "Jester", "Menagerie"],
                         event_cards=["Travelling Fair"])]),
    Game("Seacraft and Witchcraft",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fortune Teller", "Hamlet", "Horn of Plenty", "Tournament", "Young Witch"],
                         bane_cards=["Guide"]),
          ExpansionCards(name=ADVENTURES,
                         kingdom_cards=["Peasant", "Storyteller", "Swamp Hag", "Transmogrify", "Wine Merchant"],
                         event_cards=["Ferry", "Seaway"])]),
]

empires_presets = [
    Game("Zookeepers",
         [ExpansionCards(name=CORNUCOPIA,
                         kingdom_cards=["Fairgrounds", "Horse Traders", "Menagerie", "Jester", "Tournament"]),
          ExpansionCards(name=EMPIRES,
                         kingdom_cards=["Overlord", "Sacrifice", "Settlers", "Villa", "Wild Hunt"],
                         event_cards=["Annex"],
                         landmark_cards=["Colonnade"])]),
]

# TODO: nocturne/renaissance support
nocturne_presets = [

]

renaissance_presets = [

]


class Cornucopia(Expansion):
    def __init__(self, number_of_cards, banned_cards):
        self.number_of_cards = number_of_cards
        self.name = CORNUCOPIA
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
        if isinstance(other, Cornucopia):
            return None
        return other.get_preset_(EXPANSIONS.index(CORNUCOPIA))

    def draw(self):
        if self.number_of_cards == 0:
            return None
        selected_kingdom_cards = sorted(random.sample(self.kingdom_cards, self.number_of_cards))
        selected_bane_cards = ["Choose card costing from 2 to 3"] if "Young Witch" in selected_kingdom_cards else None
        return ExpansionCards(name=CORNUCOPIA,
                              kingdom_cards=selected_kingdom_cards,
                              bane_cards=selected_bane_cards)
