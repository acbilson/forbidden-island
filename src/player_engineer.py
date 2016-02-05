from constants import *
from player import *

class EngineerPlayer(Player):
  
  """ This class represents an engineer player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Engineer"]
    self.currentLocation = Constant.TileNames["BronzeGate"]

