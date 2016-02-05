from constants import *
from player import *

class DiverPlayer(Player):
  
  """ This class represents a diver player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Diver"]
    self.currentLocation = Constant.TileNames["IronGate"]

