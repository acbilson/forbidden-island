from constants import *

class Player(object):

  """ This class represents one of the players(pawns) on the board """

  def __init__(self, playerType):
    self.type = playerType
