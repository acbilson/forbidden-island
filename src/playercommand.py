from constants import *
from island import *
from enum import Enum

# class PlayerInvoker(object):
  
  # """ The invoker object for actions a Player may take """

  # def __init__(self, commands):
    # self.commands = commands
    # self.commandStack = []

  # def set_command(self, command):
    # pass

  # def undo_command(self):
    # pass

  # # What should go here?  This is the info that
  # # will be used to undo operations
  # def move(self):
    # self.commands['move'].execute()
    # pass


class PlayerReceiver(object):

  """ The base receiver object for actions a Player may take """

  def action(self):
    raise Exception("Not Implemented")

class PlayerMover(PlayerReceiver):

  def __init__(self, ):
    pass

  def action(self):

    """ Moves the player one tile """

    pass

class PlayerCommand(object):

  """ The base command object for actions a Player may take """

  def execute(self):
    raise Exception("Not implemented")

  def unexecute(self):
    raise Exception("Not implemented")


class MoveCommand(PlayerCommand):

  """ The command object to move a Player to another Tile """

  def __init__(self, mover):
    self.mover = mover

  def execute(self):

    """ Moves a user one tile """

    self.mover.action()

    pass

  def unexecute(self):

    """ returns a user one tile back from where they came """

    pass
