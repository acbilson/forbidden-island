from constants import *
from playercommand import *

class Player(object):

  """ This class represents one of the players on the board """

  def __init__(self, commands):
    self.type = None
    self.currentLocation = None
    self.commands = commands

  def move(self):
    self.commands['move'].execute()

  def undo(self):
    pass

