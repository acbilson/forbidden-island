from constants import *
from playercommand import *

class Player(object):

  """ This class represents one of the players on the board """

  def __init__(self, commands):
    self.type = None
    self.currentLocation = None
    self.commandHistory = []

  def move(self):
    move = MoveCommand(PlayerMover())
    move.execute()
    self.commandHistory.append(move)

  def shore_up(self):
    pass

  def capture_treasure(self):
    pass

  def draw_card(self):
    pass

  def trade_card(self):
    pass

  def use_card(self):
    pass

  def undo(self):
    lastCommand = self.commandHistory.pop()
    lastCommand.unexecute()

