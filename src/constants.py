from enum import Enum

class Constant():

  TileNames = {
  "FoolsLanding": "FSL",
  "GoldGate": "GGT",
  "IronGate": "IGT",
  "BronzeGate": "BGT",
  "CopperGate": "CGT",
  "SilverGate": "SGT",
  "CoralPalace": "CLP",
  "TidalPalace": "TLP",
  "CaveOfShadows": "COS",
  "CaveOfEmbers": "COE",
  "WhisperingGarden": "WGD",
  "HowlingGarden": "HGD",
  "TempleOfTheSun": "TOS",
  "TempleOfTheMoon": "TOM",
  "MistyMarsh": "MYM",
  "Watchtower": "WTR",
  "BreakersBridge": "BKB",
  "CrimsonForest": "CFS",
  "Observatory": "OBS",
  "PhantomRock": "PMR",
  "TwilightHollow": "TLH",
  "CliffsOfAbandon": "COA",
  "DunesOfDeception": "DOD",
  "LostLagoon": "LLG"
  }

  TileStatus = {
  "Raised": "   ",
  "Sunken": "SNK"}

  TreasureTiles = {
  "Empty": ("|","|"),
  "COS": ("F","F"),
  "COE": ("F","F"),
  "CLP": ("W","W"),
  "TLP": ("W","W"),
  "WGD": ("A","A"),
  "HGD": ("A","A"),
  "TOS": ("E","E"),
  "TOM": ("E","E")
  }

  PlayerType = {
  "Empty": "   ",
  "Engineer": "ENG",
  "Pilot": "PLT",
  "Diver": "DVR",
  "Messenger": "MSG",
  "Explorer": "EXP",
  "Navigator": "NAV"
  }

class PlayerAction(Enum):
  Skip = 0
  Move = 1
  ShoreUp = 2
  TradeCard = 3
  UseCard = 4
  CaptureTreasure = 5

class CardType(Enum):
  WatersRise = 1
  Sandbag = 2
  Airlift = 3
  Earth = 4
  Water = 5
  Air = 6
  Fire = 7

class LogType():

  Info = "Info"
  Warning = "Warning"
  Error = "Error"

class Board():
  Empty = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' + 
  '       |   | |   | |   | |   |        \n' + 
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' +
  '       |   | |   | |   | |   |        \n' +
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  '             /   \ /   \\              \n' +
  '             |   | |   |              \n' +
  '             \   / \   /              \n')
