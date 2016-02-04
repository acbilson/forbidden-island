from constant import *

class PlayerInvoker(object):
  
  """ The invoker object for actions a Player may take """

  def __init__(self, receiver, commands):
    self.receiver = receiver
    self.commands = commands

  def set_command(self, command):
    pass

  def undo_command(self):
    pass

  def execute_command(self):
    pass


class PlayerReceiver(object):

  """ The receiver object for actions a Player may take """

  def __init__(self):
    pass

  def action(self):
    pass

class PlayerCommand(object):

  """ The base command object for actions a Player may take """

  def __init__(self, receiver):
    self.receiver = receiver

  def execute(self):
    self.receiver.action()
    pass

  def unexecute(self):
    pass


class MoveCommand(PlayerCommand):

  """ The command object to move a Player to another Tile """

  def __init__(self):
    pass

  def execute(self):

    """ Moves a user one tile """

    pass

  def unexecute(self):

    """ returns a user one tile back from where they came """

    pass
