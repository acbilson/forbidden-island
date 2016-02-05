from constants import *
from player import *
from diverplayer import *

class PlayerFactory(object):

  def __init__(self):
    self.playerCommands = self._get_commands()

  def get_instance(self, playerType):

    options = {
      PlayerType.Diver: get_diver
    }

    execute = options.get(playerType, "nothing")
    execute()

  def get_diver(self):

    # TODO: Also add commands to Diver
    diver = DiverPlayer(None)
    return diver

  def _get_commands(self):
    commands = [MoveCommand(None)]
    return commands
