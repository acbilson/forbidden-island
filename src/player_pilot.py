from constants import *
from player import *

class PilotPlayer(Player):
  
  """ This class represents a pilot player on the board """

  def __init__(self, commands):
    Player.__init__(self, commands)
    self.type = Constant.PlayerType["Pilot"]
    self.currentLocation = Constant.TileNames["FoolsLanding"]

