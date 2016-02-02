from enum import Enum

class Player(object):

  """ This class represents one of the players on the board """

  def __init__(self, type):
    self.type = type
