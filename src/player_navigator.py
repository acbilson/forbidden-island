from constants import *
from player import *

class NavigatorPlayer(Player):
  
  """ This class represents a navigator player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Navigator"]
    self.currentLocation = Constant.TileNames["GoldGate"]

