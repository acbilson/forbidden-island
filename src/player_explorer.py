from constants import *
from player import *

class ExplorerPlayer(Player):
  
  """ This class represents an explorer player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Explorer"]
    self.currentLocation = Constant.TileNames["CopperGate"]

