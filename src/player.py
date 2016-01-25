from enum import Enum

class Player(object):

  """ This class represents one of the players(pawns) on the board """

  def __init__(self):
    pass

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


