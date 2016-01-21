from enum import Enum

class TileName():
  FoolsLanding = "FSL"
  GoldGate = "GGT"
  IronGate = "IGT"
  BronzeGate = "BGT"
  CopperGate = "CGT"
  SilverGate = "SGT"
  CoralPalace = "CLP"
  TidalPalace = "TLP"
  CaveOfShadows = "COS"
  CaveOfEmbers = "COE"
  WhisperingGarden = "WGD"
  HowlingGarden = "HGD"
  TempleOfTheSun = "TOS"
  TempleOfTheMoon = "TOM"
  MistyMarsh = "MYM"
  Watchtower = "WTR"
  BreakersBridge = "BKB"
  CrimsonForest = "CFS"
  Observatory = "OBS"
  PhantomRock = "PMR"
  TwilightHollow = "TLH"
  CliffsOfAbandon = "COA"
  DunesOfDeception = "DOD"
  LostLagoon = "LLG"

class TileStatus():
  Raised = "   "
  Sunken = "SNK"
  Lost = "LST"

class PlayerAction(Enum):
  Skip = 0
  Move = 1
  ShoreUp = 2
  TradeCard = 3
  UseCard = 4
  CaptureTreasure = 5
  
class PlayerType():
  Empty = "   "
  Engineer = "ENG"
  Pilot = "PLT"
  Diver = "DVR"
  Messenger = "MSG"
  Explorer = "EXP"
  Navigator = "NAV"

class CardType(Enum):
  WatersRise = 1
  Sandbag = 2
  Airlift = 3
  Earth = 4
  Water = 5
  Air = 6
  Fire = 7

class Treasure():
  Empty = "|"
  Earth = "E"
  Water = "W"
  Air = "A"
  Fire = "F"

class Board():
  Empty = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '      /   \ /   \ /   \ /   \\         \n' + 
  '      |   | |   | |   | |   |         \n' + 
  '      \   / \   / \   / \   /         \n' +
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
