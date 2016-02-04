from constants import *

class Player(object):

  """ This class represents one of the players on the board """

  def __init__(self, type):
    self.type = type

  def get_start_location(self):
    startLocations = [ (Constant.TileNames["FoolsLanding"], Constant.PlayerType["Pilot"]),
                       (Constant.TileNames["CopperGate"], Constant.PlayerType["Engineer"]),
                       (Constant.TileNames["SilverGate"], Constant.PlayerType["Messenger"]),
                       (Constant.TileNames["GoldGate"], Constant.PlayerType["Navigator"]),
                       (Constant.TileNames["BronzeGate"], Constant.PlayerType["Explorer"]),
                       (Constant.TileNames["IronGate"], Constant.PlayerType["Diver"])]

    return [location[0] for location in startLocations if location[1] == self.type][0]

