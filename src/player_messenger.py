from constants import *
from player import *

class MessengerPlayer(Player):
  
  """ This class represents a messenger player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Messenger"]
    self.currentLocation = Constant.TileNames["SilverGate"]

